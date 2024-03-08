from django.contrib import admin
from .models import Application, CoverLetter, Document, Interview
# Register your models here.

admin.site.register(Application)
admin.site.register(CoverLetter)
admin.site.register(Document)
admin.site.register(Interview)
