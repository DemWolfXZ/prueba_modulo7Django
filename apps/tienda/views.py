from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente ,GeneroJuego, Plataforma, Juego, Boleta,DetalleBoleta
from .forms import ClienteForm , GeneroJuegoForm, PlataformaForm, JuegoForm, CarritoClienteForm

# Create your views here.
# Vista para la página de inicio
def index(request):
    return render(request, 'index.html')

############################
#########CLIENTES##########
############################



# Vistas para listado de Clientes
def listado_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/listado_cliente.html', {'clientes': clientes})

# Vista para crear un nuevo cliente
def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_clientes')
    else:
        form = ClienteForm()
    return render(request, 'cliente/crear_cliente.html', {'form': form})

# Vista para editar un cliente existente
def editar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    form = ClienteForm(instance=cliente)
    context = {
        'form': form,
        'cliente': cliente
    }
    return render(request, 'cliente/editar_cliente.html', context)

# Vista para actualizar un cliente existente
def actualizar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    print(cliente)
    print(request.POST)
    try:
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listado_clientes')
    except Exception as e:
        print(e)
        form.add_error(None, 'Error al actualizar el cliente. Por favor, inténtalo de nuevo.')
    context = {
        'form': form,
        'cliente': cliente
    }
    return render(request, 'cliente/editar_cliente.html', context)

# Vista para eliminar un cliente existente
def eliminar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    try:
        cliente.delete()
        return redirect('listado_clientes')
    except Exception as e:
        print(e)
        return redirect('listado_clientes')
    
    
############################
#########GENERO JUEGO##########
############################

# Vistas para listado de GeneroJuego
def listado_genero_juego(request):
    genero_juegos = GeneroJuego.objects.all()
    return render(request, 'genero_juego/listado_genero_juego.html', {'genero_juegos': genero_juegos})


def crear_genero_juego(request):
    if request.method== "POST":
        form = GeneroJuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_generos_juego')
    else:
        form = GeneroJuegoForm()
    return render(request, 'genero_juego/crear_genero_juego.html', {'form':form})


def editar_genero_juego(request, id_genero):
    generojuego = get_object_or_404(GeneroJuego, id_genero=id_genero)
    form = GeneroJuegoForm(instance=generojuego)

    context = {
        'form': form,
        'generojuego': generojuego
    }
    return render(request, 'genero_juego/editar_genero_juego.html', context)


def actualizar_genero_juego(request, id_genero):
    generojuego = get_object_or_404(GeneroJuego, id_genero=id_genero)
    try:
        form = GeneroJuegoForm(request.POST, instance=generojuego)
        if form.is_valid():
            form.save()
            return redirect('listado_generos_juego')
    except Exception as e:
        print(e)
        form.add_error(None, 'Error al actualizar el genero. Por favor, inténtalo de nuevo.')
    context = {
        'form': form,
        'generojuego': generojuego
    }
    return render(request, 'genero_juego/editar_genero_juego.html', context)


def eliminar_genero_juego(request, id_genero):
    generojuego = get_object_or_404(GeneroJuego, id_genero=id_genero)
    try:
        generojuego.delete()
        return redirect('listado_generos_juego')
    except Exception as e:
        print(e)
        return redirect('listado_generos_juego')
    
    
############################
#########PLATAAFORMA##########
############################
    
# Vistas para listado de Plataforma

def listado_plataforma(request):
    plataformas = Plataforma.objects.all()
    return render(request, 'plataforma/listado_plataforma.html', {'plataformas': plataformas})

def crear_plataforma(request):
    if request.method== "POST":
        form = PlataformaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_plataforma')
    else:
        form = PlataformaForm()
    return render(request, 'plataforma/crear_plataforma.html', {'form':form})

def editar_plataforma(request, id_plataforma):
    plataforma = get_object_or_404(Plataforma, id_plataforma=id_plataforma)
    form = PlataformaForm(instance=plataforma)

    context = {
        'form': form,
        'plataforma': plataforma
    }
    return render(request, 'plataforma/editar_plataforma.html', context)

def actualizar_plataforma(request, id_plataforma):
    plataforma = get_object_or_404(Plataforma, id_plataforma=id_plataforma)
    try:
        form = PlataformaForm(request.POST, instance=plataforma)
        if form.is_valid():
            form.save()
            return redirect('listado_plataforma')
    except Exception as e:
        print(e)
        form.add_error(None, 'Error al actualizar la plataforma. Por favor, inténtalo de nuevo.')
    context = {
        'form': form,
        'plataforma': plataforma
    }
    return render(request, 'plataforma/editar_plataforma.html', context)

def eliminar_plataforma(request, id_plataforma):
    plataforma = get_object_or_404(Plataforma, id_plataforma=id_plataforma)
    try:
        plataforma.delete()
        return redirect('listado_plataforma')
    except Exception as e:
        print(e)
        return redirect('listado_plataforma')
    
    
    #############################
    #########JUEGO##########
    #############################
    
    
def listado_juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'juego/listado_juego.html', {'juegos': juegos})

def listado_juegos_cliente(request):
    juegos = Juego.objects.all()
    return render(request, 'juego/listado_juego_cliente.html', {'juegos': juegos})

def crear_juego(request):
    if request.method== "POST":
        form = JuegoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listado_juegos')
    else:
        form = JuegoForm()
    return render(request, 'juego/crear_juego.html', {'form':form})
    
def editar_juego(request, id_juego):
    juego = get_object_or_404(Juego, id_juego=id_juego)
    form = JuegoForm(instance=juego)

    context = {
        'form': form,
        'juego': juego
    }
    return render(request, 'juego/editar_juego.html', context)

def actualizar_juego(request, id_juego):
    juego = get_object_or_404(Juego, id_juego=id_juego)

    try:
        form = JuegoForm(request.POST, request.FILES, instance=juego)  # <-- IMPORTANTE request.FILES
        if form.is_valid():
            form.save()
            return redirect('listado_juegos')
    except Exception as e:
        print(e)
        form.add_error(None, 'Error al actualizar el juego. Por favor, inténtalo de nuevo.')

    context = {
        'form': form,
        'juego': juego
    }
    return render(request, 'juego/editar_juego.html', context)


def eliminar_juego(request, id_juego):
    juego = get_object_or_404(Juego, id_juego=id_juego)
    try:
        juego.delete()
        return redirect('listado_juegos')
    except Exception as e:
        print(e)
        return redirect('listado_juegos')
    
    
### carrito


def crear_carrito(request, id_juego):
    juego = get_object_or_404(Juego, id_juego=id_juego)
    carrito = request.session.get('carrito', {})
    key = str(juego.id_juego)
    if key in carrito:
        carrito[key]['cantidad'] += 1
    else:
        carrito[key] = {
            'id': juego.id_juego,
            'nombre': juego.nombre_juego,
            'precio': float(juego.precio),
            'cantidad': 1
        }
    request.session['carrito'] = carrito
    return redirect('mostrar_carrito')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    for item in carrito.values():
        item['subtotal'] = item['precio'] * item['cantidad']
    total = sum(item['subtotal'] for item in carrito.values())
    form = CarritoClienteForm()
    return render(request, 'carrito/ver_carrito.html', {
        'carrito': carrito,
        'total': total,
        'form': form
    })

def aumentar(request, id_juego):
    carrito = request.session.get('carrito', {})
    key = str(id_juego)
    
    if key in carrito:
        carrito[key]['cantidad'] += 1
    
    request.session['carrito'] = carrito
    return redirect('mostrar_carrito')

def disminuir(request, id_juego):
    carrito = request.session.get('carrito', {})
    key = str(id_juego)
    
    if key in carrito:
        carrito[key]['cantidad'] -= 1
        if carrito[key]['cantidad'] == 0:
            del carrito[key]  # elimina el item del diccionario
    
    request.session['carrito'] = carrito
    return redirect('mostrar_carrito')


def confirmar_compra(request):
    if request.method == 'POST':
        # 1. Obtener el cliente del POST
        id_cliente = request.POST.get('cliente')
        cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
        
        # 2. Obtener el carrito de la sesión
        carrito = request.session.get('carrito', {})
        
        # 3. Calcular el total general
        total = sum(item['precio'] * item['cantidad'] for item in carrito.values())
        
        # 4. Crear la Boleta en la BD
        boleta = Boleta.objects.create(
            cliente=cliente,
            total_boleta=total
        )
        
        # 5. Crear un DetalleBoleta por cada juego del carrito
        for key, item in carrito.items():
            juego = get_object_or_404(Juego, id_juego=key)
            DetalleBoleta.objects.create(
                boleta=boleta,
                juego=juego,
                cantidad=item['cantidad'],
                precio_unitario=item['precio'],
                subtotal=item['precio'] * item['cantidad']
            )
        
        # 6. Limpiar el carrito de la sesión
        del request.session['carrito']
        
        # 7. Redirigir al resumen
        return redirect('resumen_boleta', id_boleta=boleta.id_boleta)
    return redirect('mostrar_carrito')


def resumen_boleta(request, id_boleta):
    boleta = get_object_or_404(Boleta, id_boleta=id_boleta)
    detalles = DetalleBoleta.objects.filter(boleta=boleta)
    return render(request, 'carrito/resumen_boleta.html', {
        'boleta': boleta,
        'detalles': detalles
    })
    
    
def listado_boleta(request):
    boletas = Boleta.objects.all()
    """     for boleta in boletas:
        print(dir(boleta)) """
    return render(request, 'boleta/listado_boleta.html', {'boletas': boletas})