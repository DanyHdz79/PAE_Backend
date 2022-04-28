from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .models import Career, Survey, PaeUser, Question, Subject, Session, Schedule, Answer, TutorSubject
from .serializers import CareerSerializer, SurveySerializer, UserSerializer, PaeUserSerializer, QuestionSerializer, SubjectSerializer, SessionSerializer, ScheduleSerializer, AnswerSerializer, TutorSubjectSerializer

# SELECT * queries

""" class AdminsViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = (IsAuthenticated, ) """

class CareersViewSet(ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    permission_classes = (AllowAny, )

class SurveysViewSet(ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = (IsAuthenticated, )

class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

class PaeUsersViewSet(ModelViewSet):
    queryset = PaeUser.objects.all()
    serializer_class = PaeUserSerializer
    permission_classes = (IsAuthenticated, )

class QuestionsViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticated, )

class SubjectsViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (AllowAny, )

class TutorSubjectsViewSet(ModelViewSet):
    queryset = TutorSubject.objects.all()
    serializer_class = TutorSubjectSerializer
    permission_classes = (IsAuthenticated, )

class SessionsViewSet(ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = (IsAuthenticated, )

class SchedulesViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticated, )

class AnswersViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticated, )


# Specific queries

class AvailableSessionsViewSet(ModelViewSet):
    sub = 'MA1033'
    queryset = TutorSubject.objects.all()
    #innerqs = TutorSubject.objects.get(id_subject=sub)
    serializer_class = TutorSubjectSerializer
    #queryset = Schedule.objects.filter(id_user__in=TutorSubject.objects.filter(id_subject=1))
    #serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticated, )