from django.shortcuts import render
from .models import Project

# home page
def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {'projects':projects})