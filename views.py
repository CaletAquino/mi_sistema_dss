from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def login_api(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    datos = json.loads(request.body)
    usuario = datos.get("usuario")
    clave = datos.get("clave")

    user = authenticate(username=usuario, password=clave)

    if user is None:
        return JsonResponse({"error": "Usuario o contraseña incorrectos"}, status=401)

    login(request, user)
    return JsonResponse({"mensaje": "OK"})
