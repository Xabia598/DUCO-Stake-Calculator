
duco_total = float(input("Enter your CURRENT DUCO amount :: "))
duco_full_stake = (duco_total / 100) * 20
duco_after_stake = (duco_full_stake / 100) * 1

print("DUCO to stake :: " + str(duco_full_stake))
print("DUCO after stake :: " + str(duco_total + duco_after_stake))
print("DUCO gained :: " + str((duco_after_stake)))




