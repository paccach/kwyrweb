from django.shortcuts import render
from math import sqrt

def index(request):
    return render(request, 'main/index.html', {'the_title': 'solve the quadratic equation:'})

def res(request):
    if request.method == 'POST':
        try:
            the_title = 'results:'
            a = float(request.POST['a'])
            b = float(request.POST['b'])
            c = float(request.POST['c'])
            D = b * b - (4 * a * c)
            if D < 0:
                the_results = 'уравнение не имеет корней'
            elif D == 0:
                x = -b / (2 * a)
                the_results = 'уравнение имеет один корень: ' + str(x)
            else:
                x1 = (-b + sqrt(D)) / (2 * a)
                x2 = (-b - sqrt(D)) / (2 * a)
                the_results = 'уравнение имеет два корня: ' + str(x1) + ' и ' + str(x2)
        except ZeroDivisionError:
            the_results = 'ошибка a = 0'
        except Exception:
            the_results = 'ошибка'
        contents = {
            'form': request.POST,
            'the_title': the_title,
            'the_results': the_results,
        }
        return render(request, 'main/res.html', contents)