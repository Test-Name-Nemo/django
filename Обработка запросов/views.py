from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def omlet(request):
    servings = request.GET.get('servings')
    if servings:
        dishes = DATA['omlet'].copy()
        for i in dishes:
            dishes[i] *= int(servings)
        context = {'recipe': dishes}
    else:
        context = {'recipe': DATA['omlet']}
    return render(request, 'index.html', context)


def pasta(request):
    context = {'recipe': DATA['pasta']}
    return render(request, 'index.html', context)


def buter(request):
    context = {'recipe': DATA['buter']}
    return render(request, 'index.html', context)
