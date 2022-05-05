from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from .models import Career, Survey, PaeUser, Question, Subject, Session, Schedule, Answer, TutorSubject
from .serializers import CareerSerializer, SurveySerializer, UserSerializer, PaeUserSerializer, QuestionSerializer, SubjectSerializer, SessionSerializer, ScheduleSerializer, AnswerSerializer, TutorSubjectSerializer, SessionAvailabilitySerializer

# SELECT * queries
class CareersViewSet(ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    permission_classes = (AllowAny, )

class SurveysViewSet(ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

class PaeUsersViewSet(ModelViewSet):
    queryset = PaeUser.objects.all()
    serializer_class = PaeUserSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

class QuestionsViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

class SubjectsViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = (AllowAny, )

class TutorSubjectsViewSet(ModelViewSet):
    queryset = TutorSubject.objects.all()
    serializer_class = TutorSubjectSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

class SessionsViewSet(ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

class SchedulesViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

class AnswersViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )


# Specific queries
class AvailableSessionsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = TutorSubject
    serializer_class = SessionAvailabilitySerializer
    def get_queryset(self):
        queryset = TutorSubject.objects.filter(id_tutor__schedule__available = True).values('id', 'id_tutor__id__username', 'id_tutor__schedule__day_hour')
        subject = self.request.query_params.get('subject')
        if subject:
            queryset = queryset.filter(id_subject = subject)
        return queryset