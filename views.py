from django.shortcuts import render


# Create your views here.
def pd1(request):
    return render(request, 'solarpv/template/solarpv/Home.html')

def register(request):
    return render(request, 'solarpv/template/solarpv/Register.html')

def login(request):
    return render(request, 'solarpv/template/solarpv/Login.html')

def dashboard(request):
    return render(request, 'solarpv/template/solarpv/Dashboard.html')

def client(request):
    return render(request, 'solarpv/template/solarpv/Client.html')

def location(request):
    return render(request, 'solarpv/template/solarpv/Location.html')

def product(request):
    return render(request, 'solarpv/template/solarpv/Product.html')

def testStandard(request):
    return render(request, 'solarpv/template/solarpv/TestStandard.html')

def certificate(request):
    return render(request, 'solarpv/template/solarpv/Certificate.html')

