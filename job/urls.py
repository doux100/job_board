from django.urls import path
from . import views, api
app_name = 'job'
urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('add', views.job_add, name='job_add'),
    path('<str:slug>', views.job_desc, name='job_desc'),
    path('api/jobs', api.job_list_api, name='job_list_api'),
    path('api/jobs/<int:id>', api.job_detail_api, name='job_detail_api'),
    path('api/v2/jobs-add', api.Job_detail.as_view(), name='job_detail_api'),
    path('api/v2/jobs-update/<int:id>', api.Job_detail_update.as_view(), name='job_detail_api'),
]
