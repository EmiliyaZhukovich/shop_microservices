from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('refredh/', views.refresh_token, name ='refresh')
]

