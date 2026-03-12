days = input("Enter name of days:")

if days == "SATURDAY" or days == "SUNDAY" or days == "saturday" or days == "sunday":
    print(f"{days} is a holiday.")
else:
    print(f"{days} is a working day.")
