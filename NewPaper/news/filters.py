import django_filters
from .models import News
from django import forms

class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Название')
    pub_date = django_filters.DateFilter(field_name='pub_date', lookup_expr='gt', label='Позже указанной даты', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = News
        fields = ['title', 'pub_date']