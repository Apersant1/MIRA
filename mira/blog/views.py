from django.shortcuts import render


# Create your views here.
def mira(request):
    return render(request, 'blog\mira.html')
