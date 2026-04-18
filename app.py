from flask import Flask, render_template, request, jsonify
from exercises import (
    calculate_average,
    get_fastest_time,
    get_slowest_time,
    get_description,
)

app = Flask(__name__)


@app.route("/")
def index():
    """Serve the main game page."""
    return render_template("index.html")


@app.route("/api/results", methods=["POST"])
def process_results():
    """
    Process the reaction times and return calculated stats.

    Receives JSON: { "times": [234.5, 198.2, 267.8] }
    Returns JSON with stats calculated by your functions.
    """
    data = request.get_json()
    times = data.get("times", [])

    average = calculate_average(times)
    fastest = get_fastest_time(times)
    slowest = get_slowest_time(times)
    description = get_description(average)

    return jsonify({
        "average": f"{round(average)} ms",
        "fastest": f"{round(fastest)} ms",
        "slowest": f"{round(slowest)} ms",
        "description": description,
        "formatted_times": [f"{round(t)} ms" for t in times],
    })


if __name__ == "__main__":
    app.run(debug=True)
