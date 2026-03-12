working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
holidays = ["Saturday", "Sunday"]
day = input("Enter a day: ")

if day in working_days:
    print(f"{day} is a working day.")
elif day in holidays:
    print(f"{day} is a holiday.")
else:
    print(f"{day} is not a valid day.")
