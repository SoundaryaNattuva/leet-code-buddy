from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Application, CoverLetter, Document
from .forms import InterviewForm
import uuid
import boto3


S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'aryanatts-app-collector'

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('about')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

def about(request):
  return render(request, 'about.html')

@login_required
def app_index(request):
  apps = Application.objects.filter(user=request.user)
  return render(request, 'applications/index.html', { 'apps': apps })

@login_required
def app_detail(request, app_id):
  app = Application.objects.get(id=app_id)
  interview_form = InterviewForm()
  return render(request, 'applications/detail.html', {
    'app' : app,
    'interview_form': interview_form
    })

class AppCreate(LoginRequiredMixin, CreateView):
  model = Application
  fields = ['app_date', 'position', 'company', 'application_type', 'enthusiasm', 'work_arrangement', 'state', 'city', 'techstack', 'status', 'minsalary', 'maxsalary', 'notes']
  success_url = '/applications'
    
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class AppUpdate(LoginRequiredMixin, UpdateView):
  model = Application
  fields = ['app_date', 'position', 'company', 'application_type', 'enthusiasm', 'work_arrangement', 'state', 'city', 'techstack', 'status', 'minsalary', 'maxsalary', 'notes']

class AppDelete(LoginRequiredMixin, DeleteView):
  model = Application
  success_url = '/applications/'

@login_required
def add_interview(request, app_id):
  form = InterviewForm(request.POST)
  if form.is_valid():
    print("interview is VALIDDD")
    new_interview = form.save(commit=False)
    new_interview.app_id = app_id
    new_interview.save()
  print("interview is INVALIDDD")
  return redirect('app-detail', app_id=app_id)

@login_required
def cl_index(request):
  cls = CoverLetter.objects.filter(user=request.user)
  return render(request, 'coverletters/cl-index.html', { 'cls': cls })

@login_required
def cl_detail(request, cl_id):
  cl = CoverLetter.objects.get(id=cl_id)
  try: 
    doc = Document.objects.get(cl_id=cl_id) #Gives you ONE thing
  except:
    doc = None
  return render(request, 'coverletters/cl-detail.html', {
    'cl' : cl, 
    'doc': doc, 
    })

class ClCreate(LoginRequiredMixin, CreateView):
  model = CoverLetter
  fields = ['cl_date', 'position', 'letter', 'tags']
  success_url = '/coverletters'
    
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ClUpdate(LoginRequiredMixin, UpdateView):
  model = CoverLetter
  fields = ['cl_date', 'position', 'letter', 'tags']

class ClDelete(LoginRequiredMixin, DeleteView):
  model = CoverLetter
  success_url = '/coverletters'

@login_required
def add_doc(request, cl_id):
  doc_file = request.FILES.get('doc-file', None)
  if doc_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + doc_file.name[doc_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(doc_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      document = Document(url=url, cl_id=cl_id)
      cl_document = Document.objects.filter(cl_id=cl_id)
      if cl_document.first():
        cl_document.first().delete()
      document.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('cl-detail', cl_id=cl_id)

