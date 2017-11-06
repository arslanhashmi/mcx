from django.contrib import admin

# Register your models here.
from .models import Image, Visitor, VisitorAdmin

admin.site.register(Image)
admin.site.register(Visitor,VisitorAdmin)
