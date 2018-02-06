from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'bigsister/index.html', context)
