from django.shortcuts import render
from django.shortcuts import render
# Create your views here.
def index(request):
    value = 'this is test'
    print(value)
    return render(request,'index.html')