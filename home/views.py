from django.shortcuts import render
from job.filters import jobFilter
from job.models import job,Category
from django.core.paginator import Paginator
from .models import Candidates,Companies


# Create your views here.


def home(request):
    job_list = job.objects.all()
    paginator = Paginator(job_list, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    candidates=Candidates.objects.all()
    companies=Companies.objects.all()
    cat=Category.objects.all()
    for c in cat:
        c.jobcount = len(job_list.filter(category = c))
    cont = {'jobs': page_obj,'jobs_count':job_list.count,'candidates':candidates,'cat':cat,'companies':companies}
    return render(request, 'index.html',cont)

def Candidate(request,id):
    candidates_desc = Candidates.objects.get(id=id)
    return render(request, 'candidate.html',{'candidate': candidates_desc})

def Companie(request,id):
    companies = Companies.objects.get(id=id)
    return render(request, 'companies.html',{'companies': companies})
