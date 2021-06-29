from django.urls import path
from . import views


app_name = 'superheroesapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('<int:superhero_id>', views.change, name='change'),
    path('<int:superhero_id>', views.delete, name='delete')
]