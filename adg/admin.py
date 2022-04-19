from django.contrib import admin
from .models import Project,Member,Event,Tag,Blog
# Register your models here.

admin.site.register(Project)
admin.site.register(Member)
admin.site.register(Event)
admin.site.register(Tag)
admin.site.register(Blog)