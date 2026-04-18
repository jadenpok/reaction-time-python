# Reaction Lab - Python Exercises

A reaction-time game with a Python backend. Complete the functions in `exercises.py` to make it work!

## Setup

1. Run the server: `python app.py`
2. Open http://localhost:5000 in your browser
3. Play the game - you'll see placeholder results until you complete the exercises

## Tasks

**exercises.py**
- 1. `calculate_average(times)` - use a for loop to sum values, divide by length
- 2. `get_fastest_time(times)` - use a for loop to find the smallest value
- 3. `get_slowest_time(times)` - use a for loop to find the largest value
- 4. `get_description(average)` - return message based on time thresholds

## Testing Your Functions

You can test in the Python REPL:
```python
>>> from exercises import *
>>> calculate_average([200, 250, 220])
223.33...
>>> get_fastest_time([234.5, 198.2, 267.8])
198.2
>>> get_slowest_time([234.5, 198.2, 267.8])
267.8
>>> get_description(190)
"Dang. That was insane, you have lightning reflexes."
```
