from django.urls import path
from .views import CareersViewSet, SurveysViewSet, UsersViewSet, QuestionsViewSet, SubjectsViewSet, SessionsViewSet, SchedulesViewSet, AnswersViewSet, TutorSubjectsViewSet, AvailableSessionsViewSet
from rest_framework import routers

router = routers.DefaultRouter()

#router.register('admins', AdminsViewSet)
router.register('careers', CareersViewSet)
router.register('surveys', SurveysViewSet)
router.register('users', UsersViewSet)
router.register('questions', QuestionsViewSet)
router.register('subjects', SubjectsViewSet)
router.register('tutor_subjects', TutorSubjectsViewSet)
router.register('sessions', SessionsViewSet)
router.register('schedules', SchedulesViewSet)
router.register('answers', AnswersViewSet)

router.register('available_sessions', AvailableSessionsViewSet)

urlpatterns = router.urls