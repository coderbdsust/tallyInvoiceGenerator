from django.urls import path
from . import views

urlpatterns = [
    path('generate', views.generateInvoice, name='invoice-generate')
]