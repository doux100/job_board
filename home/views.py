from django.shortcuts import render
from job.models import Job,Category
from django.core.paginator import Paginator
from .models import Candidates,Companies


# Create your views here.

def getPage (request,list,num):
    paginator = Paginator(list.objects.all(), num)
    page_number = request.GET.get("page")
    obj = paginator.get_page(page_number)
    return obj


def home(request):
    job_obj=getPage(request,Job,6)
    category_obj=getPage(request,Category,4)
    companies_obj=getPage(request,Companies,4)
    
    candidates_list=Candidates.objects.all()
    
    job_list = Job.objects.all()
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
