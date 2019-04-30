import django_filters

from courses.models import Course


class CourseFilter(django_filters.FilterSet):
  # start_time = django_filters.filters.TimeFilter(field_name='timeslots__start_time', lookup_expr='exact')

  class Meta:
    model = Course
    fields = {
      'name': ['icontains'],
      'cost': ['exact'],
      'professor__name': ['icontains'],
      'timeslot__start_time':['exact'],
      'timeslot__end_time':['exact']
    }
