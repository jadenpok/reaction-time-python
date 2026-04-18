"""
Reaction Lab - Python Exercises

Implement these 4 functions to make the game work!
"""


def calculate_average(times: list[float]) -> float:
    """
    TODO 1: Calculate the average of a list of times.

    Args:
        times: A list of reaction times in milliseconds, e.g. [234.5, 198.2, 267.8]

    Returns:
        The average time as a float

    Example:
        calculate_average([200, 250, 220]) should return 223.33...

    Hint: Use a for loop to add up all values, then divide by len(times)
    """
    # Your code here

    return 0


def get_fastest_time(times: list[float]) -> float:
    """
    TODO 2: Find the fastest (smallest) time in the list.

    Args:
        times: A list of reaction times in milliseconds, e.g. [234.5, 198.2, 267.8]

    Returns:
        The smallest time in the list

    Example:
        get_fastest_time([234.5, 198.2, 267.8]) should return 198.2

    Hint: Use a for loop to check each time and keep track of the smallest one
    """
    # Your code here

    return 0


def get_slowest_time(times: list[float]) -> float:
    """
    TODO 3: Find the slowest (largest) time in the list.

    Args:
        times: A list of reaction times in milliseconds, e.g. [234.5, 198.2, 267.8]

    Returns:
        The largest time in the list

    Example:
        get_slowest_time([234.5, 198.2, 267.8]) should return 267.8

    Hint: Use a for loop to check each time and keep track of the largest one
    """
    # Your code here

    return 0


def get_description(average: float) -> str:
    """
    TODO 4: Return an encouraging message based on the average reaction time.

    Args:
        average: The average reaction time in milliseconds

    Returns:
        A string with an encouraging message

    Use these thresholds:
        - Under 180ms: "You have elite reaction speed!"
        - Under 200ms: "Dang. That was insane, you have lightning reflexes."
        - Under 225ms: "Very impressive."
        - Under 275ms: "Nice work, that was good focus."
        - Under 300ms: "Good job, that was solid work."
        - Under 350ms: "Not too shabby."
        - 350ms or more: "Need a bit of practice, but you have potential."
    """
    # Your code here

    return "Complete the Python exercises to see your results!"
