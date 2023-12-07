from django.urls import path
from .views import welcome
from .views import RecipeListView
from .views import RecipeDetailView
from .views import records
from .views import create_view
from .views import about_view
from recipes .views import RecipeListView
app_name = 'recipes'

urlpatterns = [
    path('', welcome, name='home'),
    path('list/', RecipeListView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
    path('search/', records, name='search'),
    path('create/', create_view, name='create'),
    path('about/', about_view, name='about'),
]