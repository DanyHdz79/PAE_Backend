from dataclasses import field
from xmlrpc.client import DateTime
from django.contrib.auth.models import User
from rest_framework.serializers import Serializer, ModelSerializer, ALL_FIELDS, CharField, IntegerField, EmailField, DateTimeField, BooleanField, FileField
from .models import Career, Survey, PaeUser, Question, Subject, Session, Schedule, Answer, TutorSubject, Choice
from rest_framework.authtoken.models import Token

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

class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
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

class SessionsFilesSerializer(ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'file']

class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = ALL_FIELDS

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ALL_FIELDS

class CurrentUserDataSerializer(Serializer):
    id = IntegerField()
    user_type = IntegerField()
    status = IntegerField()
    id__email = EmailField()

class SessionAvailabilitySerializer(Serializer):
    id = IntegerField()
    id_tutor__id__username = CharField()
    id_tutor__schedule__day_hour = CharField()
    service_hours = IntegerField()        

class OrderedTutorsForSpecificSessionSerializer(Serializer):
    id_tutor__id = CharField()
    service_hours = IntegerField()
    id_subject = CharField()
    id_tutor__schedule__day_hour = CharField()

class ServiceHoursSerializer(Serializer):
    id_tutor__id__first_name = CharField()
    service_hours = IntegerField()

class SessionCardSerializer(Serializer):
    id = IntegerField()
    id_subject__name = CharField()
    id_tutor__id__first_name = CharField()
    id_tutor__id__email = EmailField()
    id_student__id__first_name = CharField()
    id_student__id__email = EmailField()
    date = DateTimeField()
    spot = CharField()
    status = IntegerField()
    description = CharField()
    request_time = DateTimeField()
    file = FileField()

class SessionCardCancelValueSerializer(Serializer):
    id = IntegerField()
    id_subject__name = CharField()
    id_tutor__id__first_name = CharField()
    id_tutor__id__email = EmailField()
    id_student__id__first_name = CharField()
    id_student__id__email = EmailField()
    date = DateTimeField()
    spot = CharField()
    status = IntegerField()
    description = CharField()
    request_time = DateTimeField()
    file = FileField()
    cancel = BooleanField()

class UserDataSerializer(Serializer):
    id = IntegerField()
    id__first_name = CharField()
    career = CharField()
    semester = IntegerField()
    id__email = EmailField()

class AdminsSerializer(Serializer):
    id = IntegerField()
    id__first_name = CharField()

class SubjectsByTutorSerializer(Serializer):
    id_subject__name = CharField()

class ScheduleByTutorSerializer(Serializer):
    day_hour = CharField()
    available = BooleanField()

class RecentTutorsOfStudentSerializer(Serializer):
    id_tutor__id__first_name = CharField()

class RecentCompletedSessionSerializer(Serializer):
    id = IntegerField()
    id_tutor = CharField()
    id_student = CharField()