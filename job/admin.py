from django.contrib import admin

# Register your models here.
from .models import job, Category, apply
admin.site.register(job)
admin.site.register(Category)
admin.site.register(apply)
admin.site.site_header='job board'
admin.site.site_title='job board'
