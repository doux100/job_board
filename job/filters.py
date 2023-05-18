import django_filters
from .models import job


class jobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = job
        fields = ['title', 'job_type', 'description',
                  'Vacancy', 'experience', 'category']
