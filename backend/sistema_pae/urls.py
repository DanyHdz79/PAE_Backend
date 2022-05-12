from ast import Or
from django.urls import path
from .views import CareersViewSet, SurveysViewSet, UsersViewSet, QuestionsViewSet, SubjectsViewSet, SessionsViewSet, SchedulesViewSet, AnswersViewSet, TutorSubjectsViewSet, AvailableSessionsViewSet, PaeUsersViewSet, SessionsOfSpecificStudentViewSet, SessionsOfSpecificTutorViewSet, PendingSessionsViewSet, OrderedTutorsForSessionViewSet
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
router.register('sessions_of_specific_student', SessionsOfSpecificStudentViewSet, basename='sessions_of_specific_student')
router.register('sessions_of_specific_tutor', SessionsOfSpecificTutorViewSet, basename='sessions_of_specific_tutor')
router.register('pending_sessions', PendingSessionsViewSet, basename='pending_sessions')
router.register('ordered_tutors_for_session', OrderedTutorsForSessionViewSet, basename='ordered_tutors_for_session')

urlpatterns = router.urls