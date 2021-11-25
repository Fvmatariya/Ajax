from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add-data/',views.add_data,name='add-data'),
]
