from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.decorators.csrf import csrf_exempt

from question.models import Count_model
from django.db.models import Sum
import random

def hello(request):
    solution = request.GET.get('s', '')
    return HttpResponse(f'Hello, word {solution}  !')

def home(request):
    solution = request.GET.get('s', '')
    return render(
        request,
        template_name='registration.html',
        context={
            'imiona': [solution, 'Anna','Maciej']
        }
    )
@csrf_exempt
def result(request):

    result_views = request.POST.get('result', '0')
    a1 = request.POST.get('a1', '0')
    b1 = request.POST.get('b1', '0')
    c1 = int(a1) * int(b1)
    success = ''


    if int(a1) * int(b1) == int(result_views):
        success = "Brawo mistrzyni"
        Count_model(point=1).save()
    else:
        success= "Niestety do poprawki"
        Count_model(point=-1).save()

    a = random.randint(1, 9)
    b = random.randint(1, 9)

    return render (
        request,
        template_name='registration.html',
        context={
            'result': result_views,
            'a': a,
            'b': b,
            'a1': a1,
            'b1': b1,
            'c1': c1,
            'succes': success,
            'count': Count_model.objects.all().aggregate(Sum('point')),
        }
    )
