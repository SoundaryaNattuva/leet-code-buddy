from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Application

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def app_index(request):
  apps = Application.objects.all()
  return render(request, 'applications/index.html', { 'apps': apps })

def app_detail(request, app_id):
  app = Application.objects.get(id=app_id)
  return render(request, 'applications/detail.html', {'app' : app} )

class AppCreate(CreateView):
  model = Application
  fields = ['date', 'position', 'company', 'enthusiasm', 'workArrangement', 'state', 'city', 'techstack', 'status', 'minsalary', 'maxsalary', 'notes']
  success_url = '/applications'

class AppUpdate(UpdateView):
  model = Application
  fields = ['date', 'position', 'company', 'enthusiasm', 'workArrangement', 'state', 'city', 'techstack', 'status', 'minsalary', 'maxsalary', 'notes']

class AppDelete(DeleteView):
  model = Application
  success_url = '/applications/'