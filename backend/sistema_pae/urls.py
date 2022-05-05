from django.urls import path
from .views import CareersViewSet, SurveysViewSet, UsersViewSet, QuestionsViewSet, SubjectsViewSet, SessionsViewSet, SchedulesViewSet, AnswersViewSet, TutorSubjectsViewSet, AvailableSessionsViewSet, PaeUsersViewSet
from rest_framework import routers

router = routers.DefaultRouter()

#router.register('admins', AdminsViewSet)
router.register('careers', CareersViewSet)
router.register('surveys', SurveysViewSet)
router.register('users', UsersViewSet)
router.register('pae_users', PaeUsersViewSet)
router.register('questions', QuestionsViewSet)
router.register('subjects', SubjectsViewSet)
router.register('tutor_subjects', TutorSubjectsViewSet)
router.register('sessions', SessionsViewSet)
router.register('schedules', SchedulesViewSet)
router.register('answers', AnswersViewSet)
router.register('available_sessions', AvailableSessionsViewSet, basename='available_sessions')

urlpatterns = router.urls