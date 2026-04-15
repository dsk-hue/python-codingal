from datetime import datetime
def greet(hour=None):
    if hour is None:
        hour = datetime.now().hour

    if 4 < hour < 12:
        return "morning"
    elif 11 < hour < 16:
        return "afternoon"
    elif 15 < hour < 19:
        return "evening"
    else:
        return "night"

print(f"Hello! Good {greet()}!")