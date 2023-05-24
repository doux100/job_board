from django.shortcuts import render
from job.filters import jobFilter
from job.models import job,Category
from django.core.paginator import Paginator
from .models import Candidates,Companies


# Create your views here.

def duplication (request,list,num):
    paginator = Paginator(list, num)
    page_number = request.GET.get("page")
    obj = paginator.get_page(page_number)
    return obj


def home(request):
    job_list=job.objects.all()
    job_obj=duplication(request,job_list,6)
    category_list=Category.objects.all()
    category_obj=duplication(request,category_list,4)
    companies_list=Companies.objects.all()
    companies_obj=duplication(request,companies_list,4)
    candidates_list=Candidates.objects.all()
    for c in category_obj:
        c.jobcount = len(job_list.filter(category = c))
    cont = {'jobs': job_obj,'candidates':candidates_list,'cat':category_obj,'companies':companies_obj,'job':job_list}
    return render(request, 'index.html',cont)

def Candidate(request,id):
    candidates = Candidates.objects.get(id=id)
    return render(request, 'candidate.html',{'candidate': candidates})

def Companie(request,id):
    companies = Companies.objects.get(id=id)
    return render(request, 'companies.html',{'companies': companies})
