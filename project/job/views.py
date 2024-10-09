from django.shortcuts import render
from .models import Job 
# Create your views here.
def list_jobs (request):
    jobs = Job.objects.all() # get all Jobs using queryset api
    context =  {'jobs':jobs} # import jobs in template
    return render(request ,'job/job_list.html' , context) #show html code #import page html from templates/job

def job_descriptions (request ,id):
    job_details = Job.objects.get(id=id) # get one Job using query set api
    context =  {'job_details':job_details}
    return render(request ,'job/job_details.html' ,context)