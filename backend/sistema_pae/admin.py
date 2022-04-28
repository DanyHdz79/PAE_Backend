from django.contrib import admin
from .models import Admin, Career, Survey, PaeUser, Question, Subject, Session, Schedule, Answer, TutorSubject

# Register your models here.
admin.site.register(Admin)
admin.site.register(Career)
admin.site.register(Survey)
admin.site.register(PaeUser)
admin.site.register(Question)
admin.site.register(Subject)
admin.site.register(TutorSubject)
admin.site.register(Session)
admin.site.register(Schedule)
admin.site.register(Answer)
