from django.shortcuts import render

def hello_fixed(request):
    return render(request, 'bootstrap/base-fixed.html')

def hello_fluid(request):
    return render(request, 'bootstrap/base-fluid.html')
