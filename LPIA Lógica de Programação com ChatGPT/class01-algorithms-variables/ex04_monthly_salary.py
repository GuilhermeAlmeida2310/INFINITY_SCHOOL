monthly_salary = float(input('Insert your monthly salary: '))
weekly_hours = int(input('Insert your weekly hours: '))
monthly_hours = monthly_salary * 4
hourly_wage = monthly_salary / monthly_hours

print(hourly_wage)