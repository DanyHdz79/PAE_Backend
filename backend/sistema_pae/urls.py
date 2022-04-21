from django.urls import path
from .views import AdminsViewSet, CareersViewSet, SurveysViewSet, UsersViewSet, QuestionsViewSet, SubjectsViewSet, SessionsViewSet, SchedulesViewSet, AnswersViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('admins', AdminsViewSet)
router.register('careers', CareersViewSet)
router.register('surveys', SurveysViewSet)
router.register('users', UsersViewSet)
router.register('questions', QuestionsViewSet)
router.register('subjects', SubjectsViewSet)
router.register('sessions', SessionsViewSet)
router.register('schedules', SchedulesViewSet)
router.register('answers', AnswersViewSet)

urlpatterns = router.urls