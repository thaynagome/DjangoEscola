from django.contrib import admin
from .models import Categoria
from .models import Usuario

admin.site.register(Categoria)
admin.site.register(Usuario)