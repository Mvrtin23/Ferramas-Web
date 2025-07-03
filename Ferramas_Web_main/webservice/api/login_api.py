from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from supabase import create_client, Client
import os

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@csrf_exempt
def login_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
    
            result = supabase.table('users_profile').select('*').eq('email', email).eq('password', password).execute()
            if result.data and len(result.data) > 0:
                request.session['user_logged_in'] = True
                request.session['user_email'] = email 
                return JsonResponse({'success': True, 'message': 'Login exitoso'})
            else:
                return JsonResponse({'success': False, 'error': 'Credenciales incorrectas'}, status=401)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'error': 'Método no permitido'}, status=405)