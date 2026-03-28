import json
from django.http import JsonResponse
from pathlib import Path

FILE_PATH = Path("employees.json")

def read_employees():
    if not FILE_PATH.exists():
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def write_employees(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f)

def employeeHandler(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            employee = {
                "first_name": data.get("fname"),
                "last_name": data.get("lname"),
                "role": data.get("role"),
                "email": data.get("email"),
            }

            employees = read_employees()
            employees.append(employee)
            write_employees(employees)

            return JsonResponse({"status": "ok"})

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    # 🔹 IMPORTANT: return employees on GET
    if request.method == "GET":
        employees = read_employees()
        return JsonResponse({"employees": employees})

    return None