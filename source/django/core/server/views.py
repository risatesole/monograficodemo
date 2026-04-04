from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def hello_view(request):
    return JsonResponse({
        "message": "Hello, world!"
    })

employees = []

@csrf_exempt
def employee(request):
    global employees

    if request.method == "POST":
        try:
            body = json.loads(request.body)

            client_data = {
                "id": len(employees) + 1,
                "first_name": body.get("first_name"),
                "last_name": body.get("last_name"),
                "email": body.get("email"),
                "role": body.get("role"),
            }

            employees.append(client_data)

            return JsonResponse({
                "message": "Employee created successfully",
                "employee": client_data
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({
                "error": "Invalid JSON"
            }, status=400)

    elif request.method == "GET":
        return JsonResponse({
            "employees": employees
        })

    return JsonResponse({
        "error": "Method not allowed"
    }, status=405)
