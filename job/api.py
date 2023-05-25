from rest_framework.response import Response
from .models import Job
from .serializers import jobserializer
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def job_list_api(request):
    alljobs = Job.objects.all()
    data = jobserializer(alljobs, many=True).data
    return Response({'data': data})

@api_view(['GET'])
def job_detail_api(request,id):
    job_detail = Job.objects.get(id=id)
    data = jobserializer(job_detail).data
    return Response({'data': data})

class Job_detail(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = jobserializer

class Job_detail_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = jobserializer
    lookup_field='id'
