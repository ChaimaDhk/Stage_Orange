"""
URL configuration for Orange project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from inventaire import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.connexion , name='connexion'),
    path('sing_up',views.sing_up , name='sing_up'),
    path('ajouter',views.ajouter , name='ajouter'),
    path('base',views.base , name='base'),
    path('inventaire',views.inventaire , name='inventaire'),
    path('tableinventaire',views.tableinventaire , name='tableinventaire'),
    path('sing_in', views.sing_in, name='sing_in'),
    path('supprimer_inventaire', views.supprimer_inventaire, name='supprimer_inventaire'),
    path('edit', views.edit, name='edit'),
    path('update', views.update, name='update'),
    path('search', views.search_by_sn, name='search_by_sn'),
    path('recherche', views.searchInc_by_sn, name='searchInc_by_sn'),
    path('incident', views.incident, name='incident'),
    path('ajouterinv', views.ajouterinv, name='ajouterinv')
]
