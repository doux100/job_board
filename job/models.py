from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from accounts.models import city

# Create your models here.

jtype = (('Full Time', 'Full Time'), ('Part Time', 'Part Time'))


def imgupload(ins, fname):
    name, ext = fname.split(".")
    return "jobs/%s.%s" % (ins.id, ext)


class Job(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    job_type = models.CharField(max_length=15, choices=jtype, null=True)
    description = models.TextField(max_length=1000)
    published_at = models.DateField(auto_now=True,)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey(
        "category", on_delete=models.CASCADE, null=True,related_name='jobcategory')
    image = models.ImageField(upload_to=imgupload, null=True)
    slug = models.SlugField(blank=True, null=True)
    city = models.ForeignKey(city,on_delete=models.CASCADE,null=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category (models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = ('categories')

    def __str__(self):
        return self.title


class apply(models.Model):
    job = models.ForeignKey(Job, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    web = models.URLField(max_length=200, null=True)
    cv = models.FileField(upload_to='apply/', null=True)
    cover = models.TextField(max_length=500)
    applied_at = models.DateField(auto_now=True,)

    class Meta:
        verbose_name_plural = ('applies')

    def __str__(self):
        return self.name
