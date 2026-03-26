import math

def projectilemotion_solver(angle_deg, speed):
    g = 9.8  # gravity (m/s^2)

    # convert angle to radians
    angle_rad = math.radians(angle_deg)

    # range formula
    R = (speed**2 * math.sin(2 * angle_rad)) / g

    # max height formula
    h = (speed**2 * (math.sin(angle_rad))**2) / (2 * g)

    return R, h


from projectilemotion import projectilemotion_solver

angle = 20.0
speed = 11.0

range_dist, max_height = projectilemotion_solver(angle, speed)

print("Horizontal distance:", range_dist, "m")
print("Maximum height:", max_height, "m")