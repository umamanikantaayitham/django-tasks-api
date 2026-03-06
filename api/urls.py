from django.urls import path
from . import views

urlpatterns = [
    path('tasks/<int:pk>/', views.g_t),
    path('tasks/create/', views.c_t),
    path('tasks/update/<int:pk>/', views.u_t),
    path('tasks/delete/<int:pk>/', views.d_t),
]