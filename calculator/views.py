from django.shortcuts import render
from django.http import Http404

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipe_view(request, dish_name):
    if dish_name not in DATA:
        raise Http404(f'Recipe for {dish_name} not found')
    
    recipe = DATA[dish_name]
    servings = int(request.GET.get('servings', 1))
    
    scaled_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}
    
    context = {
        'recipe': scaled_recipe
    }
    
    return render(request, 'calculator/index.html', context)