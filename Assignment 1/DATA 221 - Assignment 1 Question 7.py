# seconds to hours --> seconds / 3600
# seconds to minutes --> seconds / 60


def time_converter(seconds):
    try:
        seconds = int(seconds)

        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        if hours < 12:
            time_period = "AM"

        else:
            time_period = "PM"


        return f"{hours} {minutes} {seconds} {time_period}"

    except ValueError:
        return "Invalid input."

print(time_converter(19067))






