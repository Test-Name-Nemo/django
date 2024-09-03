from django.shortcuts import render

DATA = {
    'омлет': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л': 0.5,
    },
    'паста': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'бутерброт': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def dish_view(request, dish):
    if dish in DATA:
        data = DATA[dish]
        servings = request.GET.get('servings')
        if servings:
            dishes = DATA[dish].copy()
            for i in dishes:
                dishes[i] *= int(servings)
            context = {
                'recipe_name': dish,
                'recipe': dishes
            }
        else:
            context = {
                'recipe_name': dish,
                'recipe': data
            }

    else:
        context = None

    return render(request, 'index.html', context)


def home_view(request):

    all_recipes = list(DATA.keys())
    context = {'all_recipes': all_recipes}

    return render(request, 'home.html', context)
