RED_LIGHT = 0
GREEN_LIGHT = 1
MAX_STRENGTH = 5

strength = int(input("Enter strength: "))

if MAX_STRENGTH - strength >= 0:
    print(GREEN_LIGHT)
else:
    print(RED_LIGHT)
