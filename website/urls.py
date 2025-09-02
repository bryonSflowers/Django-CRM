from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.simulation_record, name='record'),
    path('delete_simulation/<int:pk>', views.delete_simulation, name='delete_simulation'),
    path('add_simulation/', views.add_simulation, name='add_simulation'),
    path('update_simulation/<int:pk>', views.update_simulation, name='update_simulation'),
]