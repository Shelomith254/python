def vol_sphere(radius):
    PI=3.142
    return 4/3*radius*radius*PI
radius=float(input("Enter radius:"))
volume=vol_sphere(radius)
print("volume of sphere is:",volume)