from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1> Hey Men. How are you? </h1>')
