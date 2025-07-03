import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .supabase_client import supabase

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            username = data.get("username")
            email = data.get("email")
            rut = data.get("rut")
            phone = data.get("phone")
            password = data.get("password")

            if not all([username, email, rut, phone, password]):
                return JsonResponse({"error": "Todos los campos son obligatorios."}, status=400)

            response = supabase.table("users_profile").insert({
                "username": username,
                "email": email,
                "rut": rut,
                "phone": phone,
                "password": password
            }).execute()

            # El objeto `response` tiene el atributo `data` y `status_code`
            if response.data:
                return JsonResponse({"message": "Usuario registrado con éxito."}, status=201)
            else:
                return JsonResponse({
                    "error": "Error al registrar usuario. No se recibió data de Supabase.",
                    "supabase_response": str(response)
                }, status=500)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Método no permitido."}, status=405)