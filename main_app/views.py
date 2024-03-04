from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Application, CoverLetter, Document
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'aryanatts-app-collector'

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

def cl_index(request):
  cls = CoverLetter.objects.all()
  return render(request, 'coverletters/cl-index.html', { 'cls': cls })

def cl_detail(request, cl_id):
  cl = CoverLetter.objects.get(id=cl_id)
  return render(request, 'coverletters/cl-detail.html', {'cl' : cl} )

class ClCreate(CreateView):
  model = CoverLetter
  fields = ['date', 'position', 'letter', 'tags']
  success_url = '/coverletters'

class ClUpdate(UpdateView):
  model = CoverLetter
  fields = ['date', 'position', 'letter', 'tags']

class ClDelete(DeleteView):
  model = CoverLetter
  success_url = '/coverletters'

def add_doc(request, cl_id):
  doc_file = request.FILES.get('doc-file', None)
  if doc_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + doc_file.name[doc_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(doc_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      document = Document(url=url, id=id)
      cl_document = Document.objects.filter(id=id)
      if cl_document.first():
        cl_document.first().delete()
      document.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('cl-detail', cl_id=cl_id)