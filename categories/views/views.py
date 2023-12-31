from django.shortcuts import render

from educational_modules.models import EducationalModule


def index(request):
    """Вью для главной страницы"""

    return render(request, 'categories/index.html')


def about(request):
    """Вью для страницы about"""

    return render(request, 'categories/about.html')


def give_price(request):
    """Вью для страницы стоимость"""
    query_ed_modules = EducationalModule.objects.all()
    if len(query_ed_modules) > 0:
        min_price = min([ed.price for ed in EducationalModule.objects.all()])
        return render(request, 'categories/price.html', {'min_price': min_price})
    return render(request, 'categories/price.html')


