import math
def rect_area(wid, len):
    rounded_wid = math.ceil(wid)
    rounded_len = math.ceil(len)
    area = rounded_wid * rounded_len
    return area

def roof_cost(area, sqf_cost):
    cost = area * sqf_cost
    return cost
def estimate_green_roof(wid, len, sqf_cost):
    area = rect_area(wid, len)
    cost = roof_cost(area, sqf_cost)
    print("The area is", area, "square feet.")
    print("The total estimated cost is $" + str(cost))
estimate_green_roof(54.25, 32.8, 35)