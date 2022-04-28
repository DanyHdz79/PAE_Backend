from dataclasses import field
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, ALL_FIELDS
from .models import Admin, Career, Survey, PaeUser, Question, Subject, Session, Schedule, Answer, TutorSubject
from rest_framework.authtoken.models import Token

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
        extra_kwargs = {'password':{'required':True, 'write_only':True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user

class PaeUserSerializer(ModelSerializer):
    class Meta:
        model = PaeUser
        fields = ALL_FIELDS

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ALL_FIELDS

class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ALL_FIELDS

class TutorSubjectSerializer(ModelSerializer):
    class Meta:
        model = TutorSubject
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