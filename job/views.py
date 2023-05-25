from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Job
from django.core.paginator import Paginator
from .forms import applyform, addform
from django.contrib.auth.decorators import login_required
from .filters import jobFilter
from home.views import getPage
from job.models import Category
# Create your views here.


def job_list(request):
    job_list = Job.objects.all()
    filter = jobFilter(request.GET, queryset=job_list)    
    job_list_filter = filter.qs
    paginator = Paginator(job_list_filter, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    category_obj=getPage(request,Category,4)
    cont = {'page_obj': page_obj, 'filter': filter,'cat':category_obj}
    return render(request, 'job/list.html', cont)       


def job_desc(request, slug):
    job_desc = Job.objects.get(slug=slug)
    if request.method == 'POST':
        form = applyform(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_desc
            myform.save()
    else:
        form = applyform()
    category_obj=getPage(request,Category,4)
    cont = {'job': job_desc, 'appform': form,'cat':category_obj}
    return render(request, 'job/desc.html', cont)


@login_required
def job_add(request):
    if request.method == 'POST':
        form = addform(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('job:job_list'))
    else:
        form = addform()
    category_obj=getPage(request,Category,4)
    cont = {'job': job_desc, 'addform': form,'cat':category_obj}
    return render(request, 'job/add.html', cont)
