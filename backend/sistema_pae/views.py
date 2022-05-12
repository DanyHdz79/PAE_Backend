from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.db.models import Count, Q
from .models import Career, Survey, PaeUser, Question, Subject, Session, Schedule, Answer, TutorSubject
from .serializers import CareerSerializer, SessionCardSerializer, SurveySerializer, UserSerializer, PaeUserSerializer, QuestionSerializer, SubjectSerializer, SessionSerializer, ScheduleSerializer, AnswerSerializer, TutorSubjectSerializer, SessionAvailabilitySerializer, SessionCardSerializer, OrderedTutorsForSpecificSessionSerializer

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

class OrderedTutorsForSessionViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = TutorSubject
    serializer_class = OrderedTutorsForSpecificSessionSerializer
    def get_queryset(self):
        subject = self.request.query_params.get('subject')
        dayHour = self.request.query_params.get('dayHour')
        if subject and dayHour:
            queryset = TutorSubject.objects.filter(id_tutor__schedule__available = True,id_subject = subject, id_tutor__schedule__day_hour = dayHour).annotate(service_hours = Count('id_tutor__session', filter=Q(id_tutor__session__status = 1))).order_by('service_hours').values('id_tutor__id__first_name', 'service_hours', 'id_subject', 'id_tutor__schedule__day_hour')
            return queryset

class SessionsOfSpecificStudentViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = Session
    serializer_class = SessionCardSerializer
    def get_queryset(self):
        queryset = Session.objects.all().values('id', 'id_subject__name', 'id_tutor__id__first_name', 'id_tutor__id__email', 'id_student__id__first_name', 'id_student__id__email', 'date', 'spot', 'status')
        student = self.request.query_params.get('student')
        if student:
            queryset = queryset.filter(id_student__id = student)
        return queryset

class SessionsOfSpecificTutorViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = Session
    serializer_class = SessionCardSerializer
    def get_queryset(self):
        queryset = Session.objects.all().values('id', 'id_subject__name', 'id_tutor__id__first_name', 'id_tutor__id__email', 'id_student__id__first_name', 'id_student__id__email', 'date', 'spot', 'status')
        tutor = self.request.query_params.get('tutor')
        if tutor:
            queryset = queryset.filter(id_tutor__id = tutor)
        return queryset

class PendingSessionsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = Session
    serializer_class = SessionCardSerializer
    def get_queryset(self):
        queryset = Session.objects.filter(status = 0).values('id', 'id_subject__name', 'id_tutor__id__first_name', 'id_tutor__id__email', 'id_student__id__first_name', 'id_student__id__email', 'date', 'spot', 'status')
        return queryset