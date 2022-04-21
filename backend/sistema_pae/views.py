from rest_framework.viewsets import ModelViewSet
from .models import Admin, Career, Survey, User, Question, Subject, Session, Schedule, Answer
from .serializers import AdminSerializer, CareerSerializer, SurveySerializer, UserSerializer, QuestionSerializer, SubjectSerializer, SessionSerializer, ScheduleSerializer, AnswerSerializer

# Create your views here.
class AdminsViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class CareersViewSet(ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

class SurveysViewSet(ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuestionsViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class SubjectsViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SessionsViewSet(ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class SchedulesViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class AnswersViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
