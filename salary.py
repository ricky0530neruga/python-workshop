def calculate_salary(hours, rate):
    return hours * rate
def add_bonus(salary):
    if salary >= 30000:
        return salary + 3000
    else:
        return salary + 1000

def final_salary(hours, rate):
    return add_bonus(calculate_salary(hours, rate))

print(final_salary(160, 200))
print(final_salary(100, 200))