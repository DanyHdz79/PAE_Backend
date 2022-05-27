from contextvars import Token
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from django.db.models import Count, Q
import datetime
from .models import Career, Survey, PaeUser, Question, Subject, Session, Schedule, Answer, TutorSubject, Choice
from .serializers import CareerSerializer, SessionCardSerializer, SurveySerializer, UserSerializer, PaeUserSerializer, QuestionSerializer, SubjectSerializer, SessionSerializer, ScheduleSerializer, AnswerSerializer, TutorSubjectSerializer, SessionAvailabilitySerializer, SessionCardSerializer, OrderedTutorsForSpecificSessionSerializer, ServiceHoursSerializer, UserDataSerializer, SubjectsByTutorSerializer, ScheduleByTutorSerializer, AdminsSerializer, RecentTutorsOfStudentSerializer, CurrentUserDataSerializer, ChoiceSerializer

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

class ChoicesViewSet(ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
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
class CurrentUserDataViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = PaeUser
    serializer_class = CurrentUserDataSerializer
    def get_queryset(self):
        schoolID = self.request.query_params.get('schoolID')
        queryset = PaeUser.objects.filter(id__username = schoolID).values('id', 'user_type', "status", "id__email")
        return queryset

class AvailableSessionsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = TutorSubject
    serializer_class = SessionAvailabilitySerializer
    def get_queryset(self):
        queryset = TutorSubject.objects.filter(id_tutor__status = 0,id_tutor__schedule__available = True).annotate(service_hours = Count('id_tutor__session', filter=Q(id_tutor__session__status = 1))).order_by('service_hours').values('id', 'id_tutor__id__username', 'id_tutor__schedule__day_hour', 'service_hours')
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
            queryset = TutorSubject.objects.filter(id_tutor__status = 0,id_tutor__schedule__available = True,id_subject = subject, id_tutor__schedule__day_hour = dayHour).annotate(service_hours = Count('id_tutor__session', filter=Q(id_tutor__session__status = 1))).order_by('service_hours').values('id_tutor__id', 'service_hours', 'id_subject', 'id_tutor__schedule__day_hour')[:1]
            return queryset

class ServiceHoursViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = TutorSubject
    serializer_class = ServiceHoursSerializer
    def get_queryset(self):
        tutor = self.request.query_params.get('tutor')
        if tutor:
            queryset = TutorSubject.objects.filter(id_tutor = tutor).distinct().annotate(service_hours = Count('id_tutor__session', filter=Q(id_tutor__session__status = 1))).values('id_tutor__id__first_name', 'service_hours')
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

class StudentsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = PaeUser
    serializer_class = UserDataSerializer
    def get_queryset(self):
        student = self.request.query_params.get('student')
        queryset = PaeUser.objects.filter(user_type = 0).values('id', 'id__first_name', 'career', 'semester')
        if (student):
            queryset = queryset.filter(id = student)
        return queryset

class TutorsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = PaeUser
    serializer_class = UserDataSerializer
    def get_queryset(self):
        tutor = self.request.query_params.get('tutor')
        queryset = PaeUser.objects.filter(~Q(status = 2), user_type = 1).values('id', 'id__first_name', 'career', 'semester')
        if (tutor):
            queryset = queryset.filter(id = tutor)
        return queryset

class AdminsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = PaeUser
    serializer_class = UserDataSerializer
    def get_queryset(self):
        queryset = PaeUser.objects.filter(user_type = 2).values('id', 'id__first_name')
        return queryset

class SubjectsByTutorViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = TutorSubject
    serializer_class = SubjectsByTutorSerializer
    def get_queryset(self):
        tutor = self.request.query_params.get('tutor')
        queryset = TutorSubject.objects.filter(id_tutor = tutor).values('id_subject__name')
        return queryset

class ScheduleByTutorViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = Schedule
    serializer_class = ScheduleByTutorSerializer
    def get_queryset(self):
        tutor = self.request.query_params.get('tutor')
        queryset = Schedule.objects.filter(id_user = tutor).values('day_hour', 'available')
        return queryset

class RecentTutorsOfStudentViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = Session
    serializer_class = RecentTutorsOfStudentSerializer
    def get_queryset(self):
        date_a_month_ago = datetime.date.today()- datetime.timedelta(days = 30)
        student = self.request.query_params.get('student')
        queryset = Session.objects.filter(id_student = student, status = 3, date__gt = date_a_month_ago).values('id_tutor__id__first_name').distinct()
        return queryset

class PendingTutorsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = PaeUser
    serializer_class = UserDataSerializer
    def get_queryset(self):
        queryset = PaeUser.objects.filter(user_type = 1, status = 2).values('id', 'id__first_name', 'career', 'semester')
        return queryset

class MostRecentSurveyForStudentsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = Survey
    serializer_class = SurveySerializer
    def get_queryset(self):
        queryset = Survey.objects.filter(survey_type = 0).order_by('-creation_date')[:1]
        return queryset

class MostRecentSurveyForTutorsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = Survey
    serializer_class = SurveySerializer
    def get_queryset(self):
        queryset = Survey.objects.filter(survey_type = 1).order_by('-creation_date')[:1]
        return queryset

class QuestionsOfSpecificSurveyViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = Question
    serializer_class = QuestionSerializer
    def get_queryset(self):
        survey = self.request.query_params.get('survey')
        queryset = Question.objects.filter(id_survey = survey).order_by('id')
        return queryset

class ChoicesOfSpecificQuestionViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = Choice
    serializer_class = ChoiceSerializer
    def get_queryset(self):
        question = self.request.query_params.get('question')
        queryset = Choice.objects.filter(id_question = question).order_by('id')
        return queryset

class ScheduleByTutorAndDayHourViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = Schedule
    serializer_class = ScheduleSerializer
    def get_queryset(self):
        tutor = self.request.query_params.get('tutor')
        dayHour = self.request.query_params.get('dayHour')
        queryset = Schedule.objects.filter(id_user = tutor, day_hour = dayHour)
        return queryset

class RecentSessionsOfStudentViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = Session
    serializer_class = SessionCardSerializer
    def get_queryset(self):
        today = datetime.date.today()
        previousMonday = today - datetime.timedelta(days = today.weekday())
        student = self.request.query_params.get('student')
        queryset = Session.objects.filter(id_student__id = student, date__gte = previousMonday).values('id', 'id_subject__name', 'id_tutor__id__first_name', 'id_tutor__id__email', 'id_student__id__first_name', 'id_student__id__email', 'date', 'spot', 'status')
        return queryset

class RecentSessionsOfTutorViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    authentication_classes = (TokenAuthentication, )
    model = Session
    serializer_class = SessionCardSerializer
    def get_queryset(self):
        today = datetime.date.today()
        previousMonday = today - datetime.timedelta(days = today.weekday())
        tutor = self.request.query_params.get('tutor')
        queryset = Session.objects.filter(id_tutor__id = tutor, date__gte = previousMonday).values('id', 'id_subject__name', 'id_tutor__id__first_name', 'id_tutor__id__email', 'id_student__id__first_name', 'id_student__id__email', 'date', 'spot', 'status')
        return queryset