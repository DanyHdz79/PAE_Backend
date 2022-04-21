from django.contrib import admin
from .models import Admin, Career, Survey, User, Question, Subject, Session, Schedule, Answer

# Register your models here.
admin.site.register(Admin)
admin.site.register(Career)
admin.site.register(Survey)
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Subject)
admin.site.register(Session)
admin.site.register(Schedule)
admin.site.register(Answer)
