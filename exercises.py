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
    sum=0
    for t in times:
        sum=sum+t
    return(sum/len(times))


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
    fastest_time=100000000
    for t in times:
        if fastest_time > t:
            fastest_time=t
    return(fastest_time)


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
    slowest_time=1
    for t in times:
        if slowest_time < t:
            slowest_time=t
    return(slowest_time)


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
    def get_description(time):
        if average <180:
            return("elite")
        elif average <200:
            return("lightning")
        elif average <225:
            return("impressive")
        elif average <275:
            return("nice")
        elif average <300:
            return("good")
        elif average <350:
            return("shabby")
        elif average <100000000000000:
            return("more practice")
        

    return "Complete the Python exercises to see your results!"
