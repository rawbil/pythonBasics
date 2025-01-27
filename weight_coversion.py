weight = input("Weight: ")
unit = input("k for (Kgs) or l for (Lbs): ")
# if weight is in Kgs, convert to pounds and vice versa

# convert to kgs
if unit.lower() == "l":
    toKgs = float(weight) / 2.20462
    print("Weight in Kgs: " + str(toKgs))
# convert to lbs
elif unit.lower() == "k":
    toLbs = float(weight) * 2.20462
    print("Weight in Lbs: " + str(toLbs))
else:
    print("Wrong input. Try again..." + unit)

