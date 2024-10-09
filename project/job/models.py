from django.db import models

# Create your models here.
TYPE_JOBS = [('Full_Time' ,'Full_Time' ), ('Part_Time' ,'Part_Time' )]
class Job(models.Model): #table
    title = models.CharField (max_length=10) #column
    #location
    job_type = models.CharField (max_length=10 , choices=TYPE_JOBS ,default='Full_Time') #column
    descriptions = models.TextField(max_length=1000 ,default='')
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey('Category' ,on_delete=models.CASCADE) # one to many 
    experience = models.IntegerField(default=1) 


    def __str__(self) :
        return self.title
class Category (models.Model) : 
    name = models.CharField(max_length=25)
    def __str__(self) :
        return self.name
