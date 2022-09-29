mark = input("What is your mark for this subject: ")
try:
    mark_number = int(mark)
except:
    print("Not a number")
    exit(1)

if mark_number == 100:
    print("Congratulations")
elif mark_number >= 85:
    print("HD")
elif mark_number >= 75:
    print("D")
elif mark_number >= 65:
    print("CR")
elif mark_number >= 50:
    print("P")
else:
    print("FAIL")