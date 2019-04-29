from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action, list_route
from rest_framework.response import Response

from courses.filters import CourseFilter
from courses.serializers import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


def index(request):
  return render(request, 'index.html')


# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'questions'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.filter(
#             publish_date__lte=timezone.now(),
#         ).order_by('-publish_date')[:5]



class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Professor.objects.all()
  serializer_class = ProfessorSerializer


class TimeSlotViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = TimeSlot.objects.all()
  serializer_class = TimeSlotSerializer


class CourseViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Course.objects.all()
  serializer_class = CourseSerializer
  filter_backends = (filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter)
  # TODO: Use this filter to support custom filtering [case-insensitive]
  filterset_class = CourseFilter
  # TODO: return headers, filters with the data [user renderer maybe?]

  # filterset_fields = ('name', 'professors__name')

  search_fields = ('name', 'professor__name')
  ordering_fields = ('name', 'cost')
  ordering = ('name',)

  # TODO: is it right?

  @list_route()
  def table_attr(self, request):
    data = {
      'filters': [
        {
          'name': 'name',
          'type': 'text',
          'label': 'Name',

        },
        {
          'name': 'cost',
          'type': 'number',
          'label': 'Cost',
        },
        {
          'name': 'professor__name',
          'type': 'text',
          'label': 'Professor',
        }
      ],
      'headers': [
        {'name': 'name', 'label': 'Name'},
        {'name': 'cost', 'label': 'Cost'},
        {'name': 'professor', 'label': 'Professor'},
      ]
    }
    return Response(data)
