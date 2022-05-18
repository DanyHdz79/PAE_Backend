from ast import Or
from django.urls import path
from .views import CareersViewSet, SurveysViewSet, UsersViewSet, QuestionsViewSet, SubjectsViewSet, SessionsViewSet, SchedulesViewSet, AnswersViewSet, TutorSubjectsViewSet, AvailableSessionsViewSet, PaeUsersViewSet, SessionsOfSpecificStudentViewSet, SessionsOfSpecificTutorViewSet, PendingSessionsViewSet, OrderedTutorsForSessionViewSet, ServiceHoursViewSet, StudentsViewSet, TutorsViewSet, SubjectsByTutorViewSet, ScheduleByTutorViewSet, AdminsViewSet, RecentTutorsOfStudentViewSet, CurrentUserDataViewSet
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
router.register('service_hours', ServiceHoursViewSet, basename='service_hours')
router.register('students', StudentsViewSet, basename='students')
router.register('tutors', TutorsViewSet, basename='tutors')
router.register('admins', AdminsViewSet, basename='admins')
router.register('subjects_by_tutor', SubjectsByTutorViewSet, basename='subjects_by_tutor')
router.register('schedule_by_tutor', ScheduleByTutorViewSet, basename='schedule_by_tutor')
router.register('recent_tutors_of_student', RecentTutorsOfStudentViewSet, basename='recent_tutors_of_student')
router.register('current_user_data', CurrentUserDataViewSet, basename='current_user_data')

urlpatterns = router.urls