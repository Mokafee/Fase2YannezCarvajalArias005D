from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.contacto, name='contacto'),
    path('',views.index, name='index'),
]

urlpatterns+=[
    path('contacto/create/', views.ContactoCreate.as_view(), name='contacto_create'),
    path('contacto/<int:pk>/update/', views.ContactoUpdate.as_view(), name='contacto_update'),
    path('contacto/<int:pk>/delete/', views.ContactoDelete.as_view(), name='contacto_delete'),
]