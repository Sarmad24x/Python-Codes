'''def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Find the next 20 leap years
current_year = 2023
leap_years_found = 0

print("Next 20 Leap Years:")
while leap_years_found < 20:
    if is_leap_year(current_year):
        print(current_year)
        leap_years_found += 1
    current_year += 1'''

c_year =2024
leap_years=0

while(leap_years<20):
    if(c_year%4==0 and c_year%100 ==0) or (c_year%400==0):
        print(c_year)
        leap_years +=1
    c_year+=1