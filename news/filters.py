import django_filters
from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter
from .models import Post, Category


class PostFilter(FilterSet):
    title = django_filters.CharFilter(
        field_name='heading',
        lookup_expr='icontains',
        label='Заголовок'
    )

    category = django_filters.ModelChoiceFilter(
        field_name='post_category',
        queryset=Category.objects.all(),
        label='Категории',
        empty_label='Выберите категорию ',
    )

    date_after = DateTimeFilter(
        field_name='time',
        lookup_expr='gt',
        label='Дата',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )