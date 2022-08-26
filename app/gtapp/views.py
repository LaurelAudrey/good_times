from django.shortcuts import render

# Create your views here.
def hello_gt(request):
    return render(request, 'gtapp/hello_gt.html', {})