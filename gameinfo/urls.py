"""
URL configuration for WikiTheForest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('menu/', views.menu_view, name='menu'),
    path('registrarse/', views.registrarse_view, name='registrarse'),
    path('animales/', views.animales_view, name='animales'),
    path('armas/', views.armas_view, name='armas'),
    path('construcciones/', views.construcciones_view, name='construcciones'),
    path('consumibles/', views.consumibles_view, name='consumibles'),
    path('enemigos/', views.enemigos_view, name='enemigos'),
    path('flora/', views.flora_view, name='flora'),
    path('forowiki/', views.forowiki_view, name='forowiki'),
    path('historia/', views.historia_view, name='historia'),
    path('logros/', views.logros_view, name='logros'),
    path('lugarestf/', views.lugarestf_view, name='lugarestf'),
    path('micuentatf/', views.micuentatf_view, name='micuentatf'),
    path('recuperacontra/', views.recuperacontra_view, name='recuperacontra'),
    path('registrase_wiki/', views.registrase_wiki_view, name='registrase_wiki'),     
]
