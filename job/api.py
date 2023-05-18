from rest_framework.response import Response
from .models import job
from .serializers import jobserializer
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def job_list_api(request):
    alljobs = job.objects.all()
    data = jobserializer(alljobs, many=True).data
    return Response({'data': data})

@api_view(['GET'])
def job_detail_api(request,id):
    job_detail = job.objects.get(id=id)
    data = jobserializer(job_detail).data
    return Response({'data': data})

class Job_detail(generics.ListCreateAPIView):
    queryset = job.objects.all()
    serializer_class = jobserializer

class Job_detail_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = job.objects.all()
    serializer_class = jobserializer
    lookup_field='id'
