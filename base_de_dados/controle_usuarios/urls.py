"""controle_usuarios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuarios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('arduino/', views.arduino),
    path('cadastro/', views.cadastro),
    path('cobol/', views.cobol),
    path('cursos/', views.cursos, name='cursos'),
    path('descontos/', views.descontos),
    path('designgrafico/', views.designgrafico),
    path('java/', views.java),
    path('logica/', views.logica),
    path('manutencao/', views.manutencao),
    path('noticias/', views.noticias),
    path('python/', views.python),
    path('ruby/', views.ruby),
    path('arduino/', views.arduino),
    path('aluno/', views.aluno),
    path('professor/', views.professor),
    path('usuario/', views.usuario),
    path('disciplina/', views.disciplina),

]
