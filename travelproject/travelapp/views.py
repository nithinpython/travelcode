from django.shortcuts import render, HttpResponse
from .models import place, meet


# Create your views here.
def demo(request):
    obj = place.objects.all()
    obj1 = meet.objects.all()
    return render(request, 'index.html', {'result': obj,
                                          'team': obj1})

# def about(request):
#     return render(request,'result.html')
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,'result.html',{'obj':res})
