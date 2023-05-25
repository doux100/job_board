from django.contrib import admin

# Register your models here.
from .models import Job, Category, apply
admin.site.site_header='Job Board Admin Panel'
class InlineCategory(admin.StackedInline):
    model=Job
    extra=1
class JobAdmin(admin.ModelAdmin):
    list_display=('title','owner','vacancy')
    list_filter=('owner','vacancy')

class CategoryAdmin(admin.ModelAdmin):
        inlines=[InlineCategory]

admin.site.register(Job,JobAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(apply)
