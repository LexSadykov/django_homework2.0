

from django.urls import path
from calculator.views import recipe_view
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Recipe Service! Please specify a recipe, e.g., /omlet/")

urlpatterns = [
    path('', index, name='index'),  
    path('<str:dish_name>/', recipe_view, name='recipe'),
]