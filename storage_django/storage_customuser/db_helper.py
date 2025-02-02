from .models import CustomUser


# listando informações sobre os usuários
def list_employee_info():
    """
    Search for all CustomUser objects and list as a dictionary.
    """
    employees = CustomUser.objects.all()
    employee_info = {}
    
    for employee in employees:
        employee_info[employee.id] = {
            "first_name": employee.first_name,
            "last_name": employee.last_name,
            "email": employee.email,
            "role": employee.role,
            "state": employee.state,
            "phone_number": employee.phone_number,
            "registration": employee.registration,
        }
    return employee_info
        