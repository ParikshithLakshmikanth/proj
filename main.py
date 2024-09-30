wd = int(input("Enter Total no of Working Days: "))
ad = int(input("Enter Total no of Days Absent : "))
pd = wd-ad

if (pd/wd)*100 < 75.0:
    print("Not eligible")
else:
    print("Eligible")