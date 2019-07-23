from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required
def index(request, path):
    return render(request, 'index.html')
