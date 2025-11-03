def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
        return True
    else:
        print(f"{year} is not a leap year")
        return False
        
is_leap_year(1700)