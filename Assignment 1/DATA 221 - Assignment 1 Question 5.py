import math

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    if radiusOfCircle1 >= 0 and radiusOfCircle2 >= 0:
        areaOfCircle1 = math.pi * (radiusOfCircle1 ** 2)
        areaOfCircle2 = math.pi * (radiusOfCircle2 ** 2)

        return areaOfCircle1, areaOfCircle2

    else:
        return "Both radii must be positive to calculate the area of circle."

radiusOfCircle1 = -12
radiusOfCircle2 = 20

print(circleAreaCoverage(radiusOfCircle1, radiusOfCircle2))


# pi * r^2





