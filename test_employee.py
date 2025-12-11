from employee import employee_details
def test_employee_details():
    expected_output=(
        "Employee_Name:Ratna\n"
        "Employee_ID:E1001\n"
        "Department:IT\n"
        "Salary:55000"
    )
    assert employee_details("Ratna","E1001","IT",55000)==expected_output