from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('applications/', views.app_index, name = 'app-index'),
  path('applications/<int:app_id>/', views.app_detail, name = 'app-detail'),
  path('applications/create/', views.AppCreate.as_view(), name='app-create'),
  path('applications/<int:pk>/update/', views.AppUpdate.as_view(), name='app-update'),
  path('applications/<int:pk>/delete/', views.AppDelete.as_view(), name='app-delete'),
  # path('application/<int:app_id>/add-interview/', views.add_interview, name='add-interview'),
  path('coverletters/', views.cl_index, name='cl-index'),
  path('coverletters/<int:cl_id>/', views.cl_detail, name='cl-detail'),
  path('coverletters/create/', views.ClCreate.as_view(), name='cl-create'),
  path('coverletters/<int:pk>/update/', views.ClUpdate.as_view(), name='cl-update'),
  path('coverletters/<int:pk>/delete/', views.ClDelete.as_view(), name='cl-delete'),
  path('coverletters/<int:cl_id>/add-doc/', views.add_doc, name='add-doc'),
]