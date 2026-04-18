const TOTAL_ROUNDS = 3;
const WAIT_MIN_MS = 2000;
const WAIT_RANDOM_MS = 1750;

const startScreen = document.getElementById("test-selection");
const playingState = document.getElementById("playing-state");
const resultsState = document.getElementById("results-state");
const startButton = document.getElementById("start-button");
const tryAgainButton = document.getElementById("different-test-button");
const shareButton = document.getElementById("share-button");

const reactionPanel = document.getElementById("reaction-panel");
const hudContent = document.getElementById("hud-content");
const panelPhase = document.getElementById("panel-phase");
const panelInstruction = document.getElementById("panel-instruction");

const averageTime = document.getElementById("average-time");
const reactionRange = document.getElementById("reaction-range");
const reactionDescription = document.getElementById("reaction-description");
const roundTimeElements = Array.from(
  document.querySelectorAll("[data-round-time]"),
);

let currentRound = 0;
let isReady = false;
let startTime = 0;
let results = [];
let readyTimeoutId = null;

function formatMilliseconds(value) {
  return `${Math.round(value)} ms`;
}

function setPanel(className, phaseText, instructionText) {
  reactionPanel.className = `game-panel ${className}`;
  panelPhase.textContent = phaseText;
  panelInstruction.textContent = instructionText;
  hudContent.textContent = currentRound === 0 ? "" : `Round ${currentRound} of ${TOTAL_ROUNDS}`;
}

function startGame() {
  startScreen.classList.add("hidden");
  playingState.classList.remove("hidden");
  document.body.classList.add("playing-mode");
  currentRound = 0;
  results = [];
  startRound();
}

function startRound() {
  currentRound += 1;
  isReady = false;
  setPanel("waiting", "WAIT", "");

  const delay = WAIT_MIN_MS + Math.random() * WAIT_RANDOM_MS;

  readyTimeoutId = setTimeout(() => {
    isReady = true;
    startTime = performance.now();
    setPanel("ready", "TAP!", "");
    readyTimeoutId = null;
  }, delay);
}

function handlePanelClick() {
  if (!isReady) {
    clearTimeout(readyTimeoutId);
    setPanel("early", "TOO SOON!", "Tap to retry");
    setTimeout(() => startRound(), 1000);
    return;
  }

  const reactionTime = performance.now() - startTime;
  results.push(reactionTime);

  setPanel("result", formatMilliseconds(reactionTime), "");

  setTimeout(() => {
    if (currentRound < TOTAL_ROUNDS) {
      startRound();
    } else {
      showResults();
    }
  }, 1500);
}

// Send results to Python backend for processing
async function showResults() {
  try {
    const response = await fetch("/api/results", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ times: results }),
    });
    const data = await response.json();

    averageTime.textContent = data.average;
    reactionRange.textContent = `Fastest: ${data.fastest} · Slowest: ${data.slowest}`;
    reactionDescription.textContent = data.description;

    data.formatted_times.forEach((time, index) => {
      roundTimeElements[index].textContent = time;
    });
  } catch (error) {
    console.error("Error fetching results:", error);
    averageTime.textContent = "Error";
    reactionPercentile.textContent = "Could not process results";
    reactionDescription.textContent = "Check that the Python server is running";
  }

  playingState.classList.add("hidden");
  resultsState.classList.remove("hidden");
  document.body.classList.remove("playing-mode");
}

function showStartScreen() {
  resultsState.classList.add("hidden");
  startScreen.classList.remove("hidden");
  document.body.classList.remove("playing-mode");
  currentRound = 0;
  results = [];
}

// Event listeners
startButton.addEventListener("click", startGame);
tryAgainButton.addEventListener("click", showStartScreen);
reactionPanel.addEventListener("click", handlePanelClick);

shareButton.addEventListener("click", async () => {
  const text = `${averageTime.textContent} - ${reactionPercentile.textContent}`;

  if (navigator.share) {
    try {
      await navigator.share({
        title: "Reaction Lab",
        text: text,
        url: window.location.href,
      });
    } catch (error) {
      if (error.name !== "AbortError") {
        console.error("Share failed:", error);
      }
    }
    return;
  }

  try {
    await navigator.clipboard.writeText(`${text} ${window.location.href}`);
    shareButton.textContent = "Copied!";
    setTimeout(() => {
      shareButton.textContent = "Share";
    }, 2000);
  } catch (error) {
    console.error("Failed to copy:", error);
  }
});
