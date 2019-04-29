from django.contrib.auth.models import User
from rest_framework import serializers

from courses.models import *


# TODO: Make sure of Validation


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('url', 'username', 'email')


class ProfessorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Professor
    fields = ('url', 'name',)


class TimeSlotSerializer(serializers.ModelSerializer):
  class Meta:
    model = TimeSlot
    fields = ('url', 'start_time', 'end_time')


class CourseSerializer(serializers.ModelSerializer):
  name = serializers.CharField(max_length=30, required=True)
  cost = serializers.FloatField(required=True)
  # TODO: this relation is not right
  timeslots = TimeSlotSerializer(read_only=True, source='timeslot_set', many=True)

  class Meta:
    model = Course
    fields = ('url', 'id', 'name', 'cost', 'professor', 'timeslots')

#TODO: get professor name
  def ger_professor(self,obj):
    return obj.professor__name
