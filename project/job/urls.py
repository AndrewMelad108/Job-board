from django.urls import path
from . import views
urlpatterns = [
    path('',views.list_jobs , name="list_jobs" ),
    path('<int:id>/', views.job_descriptions, name="job_descriptions"),
]
