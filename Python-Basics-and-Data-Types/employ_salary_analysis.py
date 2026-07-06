# Employee Salary Analysis
# Problem Statement
# Read salary data for N employees and perform the following operations.
# Input
# •	Number of employees 
# •	Employee salaries 
# ________________________________________
# Perform
# 1. Validate the input
# Reject:
# •	Strings 
# •	Negative salary 
# •	Empty input 
# •	Invalid decimal format 
# ________________________________________
# 2. Convert salary into float.
# ________________________________________
# 3. Calculate
# •	Average Salary 
# •	Maximum Salary 
# •	Minimum Salary 
# •	Total Salary 
# ________________________________________
# 4. Display salary statistics.
# Example:
# Average Salary : 45000.50

# Maximum Salary : 78000

# Minimum Salary : 25000

# Total Salary : 225002.50
# ________________________________________
# 5. Display salary category.
# Example:
# Below 30000
# → Low Salary

# 30000–60000
# → Medium Salary

# Above 60000
# → High Salary
# ________________________________________
# 6. Count
# •	Number of High Salary employees 
# •	Number of Medium Salary employees 
# •	Number of Low Salary employees 
# ________________________________________
# 7. Print salaries in sorted order.
# Ascending and descending.
# ________________________________________
# 8. Find the second highest salary.
# ________________________________________
# 9. Remove duplicate salaries.
# ________________________________________
# 10. Display salary statistics using appropriate Python data structures.

import math


def salary_analysis(employ_nums,salaries):

    # 1. Validating the input
    if not isinstance(employ_nums,int):
        raise TypeError("Number of employees must be integer")
    
    if not all(isinstance(x,int) for x in salaries):
        raise TypeError("Employees salary must be integer")
    
    if any(x<0 for x in salaries):
        raise ValueError("Salaries must be greater than 0")
    
    if not salaries:
        raise ValueError("Salaries should not be empty")
    
    if employ_nums != len(salaries):
        raise ValueError(f"Expected {employ_nums} salaries, but recieved only {len(salaries)}")
    
    # 2. Converting Salaries into float
    salaries = [float(x) for x in salaries]

    # 3. Calculating
    # •	Average Salary

    average_salary = round(sum(salaries)/employ_nums,2)

    # •	Maximum Salary
    maximun_salary = max(salaries)

    # •	Minimum Salary
    minimum_salary = min(salaries)

    # •	Total Salary
    total_salary = sum(salaries)

    # 5. Display salary category.
    salary_category = []
    for x in salaries:
        if x < 30000:
            salary_category.append("Low Salary")
        elif x >= 30000 and x <= 60000:
            salary_category.append("Medium Salary")
        else:
            salary_category.append("High Salary")

    # 6. Salary Category Count
 
    high_salary_emp = 0
    medium_salary_emp = 0
    low_salary_emp = 0

    for i in salary_category:
        if i == "High Salary":
            high_salary_emp += 1
        elif i == "Medium Salary":
            medium_salary_emp += 1
        elif i == "Low Salary":
            low_salary_emp += 1


    # 7. Print salaries in sorted order. Ascending and descending.

    salaries_asc = list(sorted(salaries))
    salaries_des = list(sorted(salaries,reverse=True))
    
    # Find the second highest salary.
    second_highest_salary = sorted(set(salaries_des))[-2]

    # 9. Remove duplicate salaries.
    duplicate_salary = set()
    unique_salaries = []

    for i in salaries:
        if i not in duplicate_salary:
            unique_salaries.append(i)
            duplicate_salary.add(i)
        

    return f"""
Number of Employees : {employ_nums}
Salary of Employees : {salaries}

Average Salary : {average_salary}
Maximum Salary : {maximun_salary}
Minimum Salary : {minimum_salary}
Total Salary : {total_salary}

Salary Category : {salary_category}

Salary Category Count ->
High Salary Employees : {high_salary_emp}
Medium Salary Employees : {medium_salary_emp}
Low Salary Employees : {low_salary_emp}

Salary in ascending order : {salaries_asc}
Salary in descending order : {salaries_des}

Second Highest Salary : {second_highest_salary}

Unique Salaries : {unique_salaries}
"""


print(salary_analysis(6,[10000,20000,30000,40000,40000,65000]))