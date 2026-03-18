from django.contrib import admin
from .models import Cliente, GeneroJuego, Plataforma, Juego
# Register your models here.
admin.site.register(Cliente)
admin.site.register(GeneroJuego)
admin.site.register(Plataforma)
admin.site.register(Juego)
""" admin.site.register(Boleta)
admin.site.register(DetalleBoleta) """

"""
Modificaciones del panel administrativo de Django
"""
admin.site.site_header = "Panel administrativo - GameStore"
admin.site.site_title = "GameStore"
admin.site.index_title = "Panel Administrativo"


