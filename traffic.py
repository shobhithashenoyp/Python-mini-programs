color = input("Enter the traffic light color (red, yellow, green): ")
a = color.lower()
if a=="red":
    print("stop")
elif a=="yellow":
    print("ready")
elif a=="green":
    print("go")
else:
    print("invalid color")
