from django.shortcuts import redirect, render
from django.urls import reverse
from .models import job
from django.core.paginator import Paginator
from .forms import applyform, addform
from django.contrib.auth.decorators import login_required
from .filters import jobFilter

# Create your views here.


def job_list(request):
    job_list = job.objects.all()
    filter = jobFilter(request.GET, queryset=job_list)
    job_list_filter = filter.qs
    paginator = Paginator(job_list_filter, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    cont = {'jobs': page_obj, 'filter': filter}
    return render(request, 'job/list.html', cont)


def job_desc(request, slug):
    job_desc = job.objects.get(slug=slug)
    if request.method == 'POST':
        form = applyform(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_desc
            myform.save()
    else:
        form = applyform()
    cont = {'job': job_desc, 'appform': form}
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

    cont = {'job': job_desc, 'addform': form}
    return render(request, 'job/add.html', cont)
