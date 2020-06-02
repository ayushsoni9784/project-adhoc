from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def services(request):
    return render(request, 'services.html', {})

@login_required
def buildimage(request):
    return render(request, 'CodeContainerization.html', {})