from dataclasses import field
from rest_framework.serializers import ModelSerializer, ALL_FIELDS
from .models import Admin, Career, Survey, User, Question, Subject, Session, Schedule, Answer

class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = ALL_FIELDS

class CareerSerializer(ModelSerializer):
    class Meta:
        model = Career
        fields = ALL_FIELDS
        
class SurveySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = ALL_FIELDS

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ALL_FIELDS

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ALL_FIELDS

class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ALL_FIELDS
        
class SessionSerializer(ModelSerializer):
    class Meta:
        model = Session
        fields = ALL_FIELDS

class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = ALL_FIELDS

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ALL_FIELDS