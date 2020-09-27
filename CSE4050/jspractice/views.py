from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError

# Main view
def jspractice(request):
    return render(request, 'js_practice.html')
