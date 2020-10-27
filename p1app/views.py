from django.shortcuts import render
from .models import Pi
# Create your views here.
def index(request):
    context=dict()
    all_pi = Pi.objects.all()
    context['all_pi'] = all_pi

    return render(request,"index.html", context) 

def second(request):
    return render(request, 'second.html')
    