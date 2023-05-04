import employee_info

def test_get_employees_by_age_range():
    expected_result = [{'age': 25, 'department': 'Marketing', 'name': 'Jane', 'salary': 60000},
 {'age': 23, 'department': 'Marketing', 'name': 'Mary', 'salary': 56000}]
    assert employee_info.get_employees_by_age_range(age_lower_limit=20, age_upper_limit=30) == expected_result

def test_calculate_average_salary():
    expected_avg = 60166.666666666664
    assert employee_info.calculate_average_salary() == expected_avg

def test_get_employees_by_dept():
    expected_employees = [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    assert employee_info.get_employees_by_dept(department="Engineering") == expected_employees
