current_year = 2024
leap_years_found = 0

while leap_years_found < 20:
    if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
        print(current_year)
        leap_years_found += 1
    current_year += 1
