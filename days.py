days = int(input("Enter the number of days: "))

years = days // 365
remaining = days % 365
weeks = remaining // 7
rem_days = remaining % 7

print(years, "years,", weeks, "weeks,", rem_days, "days")