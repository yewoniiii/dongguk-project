from django.shortcuts import render
from requests import request
from django.views.generic import (
    View,
)

def Index(request):
    return render(request, 'care/index.html')