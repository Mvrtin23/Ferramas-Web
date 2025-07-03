import json
import mercadopago
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .mindicador import get_dolar_value


# Inicio
def welcome(request):
    productos = Producto.objects.all()
    dolar = get_dolar_value()
    return render(request, 'views/welcome.html', {
        'productos': productos,
        'dolar': dolar
    })

# Cerrar sesión
def logout_view(request):
    request.session.flush()
    return redirect('welcome')

# Formulario de registro
def register(request):
    return render(request, 'views/register.html')

# MOstrar formulario
def show_register(request):
    return render(request, "register.html")

# Mostrar catalogo
def lista_productos(request):
    productos = Producto.objects.all()
    dolar = get_dolar_value()
    return render(request, 'productos.html', {
        'productos': productos,
        'dolar': dolar
    })

# Agregar producto
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = request.session.get('carrito', {})

    if str(producto_id) in carrito:
        carrito[str(producto_id)] += 1
    else:
        carrito[str(producto_id)] = 1

    request.session['carrito'] = carrito
    return redirect('lista_productos')

# MOstrar carrito
def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos = []
    total = 0

    for producto_id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, id=producto_id)
        subtotal = producto.precio * cantidad
        total += subtotal
        productos.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })

    return render(request, 'carrito.html', {'productos_carrito': productos, 'total': total})

def reducir_cantidad(request, producto_id):
    carrito = request.session.get('carrito', {})
    producto_id_str = str(producto_id)

    if producto_id_str in carrito:
        if carrito[producto_id_str] > 1:
            carrito[producto_id_str] -= 1
        else:
            carrito.pop(producto_id_str)
        request.session['carrito'] = carrito
    return redirect('ver_carrito')

# Elimnar producto del carrito
def eliminar_producto(request, producto_id):
    carrito = request.session.get('carrito', {})
    producto_id_str = str(producto_id)

    if producto_id_str in carrito:
        carrito.pop(producto_id_str)
        request.session['carrito'] = carrito
    return redirect('ver_carrito')

@csrf_exempt
def pagar_con_mercado_pago(request):
    if request.method == 'POST':
        sdk = mercadopago.SDK("APP_USR-6027495490466892-052603-49d093ab484bf10e98619d261b71d527-2460988580")
        try:
            data = json.loads(request.body)
            productos = data.get('productos', [])
            
            preference_data = {
                "items": productos,
                "back_urls": {
                    "success": "https://ee4e-2803-c600-d103-a22f-a12c-c012-b0c7-7b7b.ngrok-free.app/pago-exitoso/",
                    "failure": "https://ee4e-2803-c600-d103-a22f-a12c-c012-b0c7-7b7b.ngrok-free.app/pago-fallido/",
                    "pending": "https://ee4e-2803-c600-d103-a22f-a12c-c012-b0c7-7b7b.ngrok-free.app/pago-pendiente/"
                },
                "auto_return": "approved",
            }
            preference_response = sdk.preference().create(preference_data)
            preference = preference_response["response"]

            return JsonResponse({"init_point": preference["init_point"]})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)

def pago_exitoso(request):
    return render(request, 'vistas_mpago/pago_exitoso.html')

def pago_fallido(request):
    return render(request, 'vistas_mpago/pago_fallido.html')

def pago_pendiente(request):
    return render(request, 'vistas_mpago/pago_pendiente.html')

def obtener_productos_carrito_json(request):
    carrito = request.session.get('carrito', {})
    productos = []

    for producto_id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, id=producto_id)
        productos.append({
            "title": producto.nombre,
            "quantity": cantidad,
            "unit_price": float(producto.precio)
        })

    return JsonResponse({"productos": productos})
