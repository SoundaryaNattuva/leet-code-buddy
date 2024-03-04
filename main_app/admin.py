from django.contrib import admin
from .models import Application, CoverLetter, Document
# Register your models here.

admin.site.register(Application)
admin.site.register(CoverLetter)
admin.site.register(Document)
