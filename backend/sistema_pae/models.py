from django.db import models
from django.contrib.auth.models import User

# Create your models here.
""" class Admin(models.Model):
    id = models.EmailField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=256) #ecrypt password

    def __str__(self):
        return self.id + ' ' + self.name """

class Career(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.id

class Survey(models.Model):
    creation_date = models.DateTimeField()
    survey_type = models.IntegerField()

    def __str__(self):
        return self.id

class PaeUser(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    semester = models.IntegerField(null = True)
    career = models.ForeignKey(Career, on_delete=models.RESTRICT, null = True)
    user_type = models.IntegerField() #0 - Student  1 - Tutor  2 - Admin
    status = models.IntegerField() #0 - Available  1 - LockedBySurvey  2 - NotVerified

    def __str__(self):
        return str(self.id)

class Subject(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    id_career = models.ManyToManyField(Career)
    semester = models.IntegerField()

    def __str__(self):
        return self.id

class TutorSubject(models.Model):
    id_tutor = models.ForeignKey(PaeUser, on_delete=models.CASCADE)
    id_subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_tutor) + ' - ' + str(self.id_subject)


class Schedule(models.Model):
    id_user = models.ForeignKey(PaeUser, on_delete=models.CASCADE)
    day_hour = models.CharField(max_length=4)
    available = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id_user) + ' - ' + self.day_hour

class Question(models.Model):
    id_survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    question_type = models.IntegerField()

    def __str__(self):
        return self.id_survey + ' - ' + self.question + ' - ' +self.question_type

class Choice(models.Model):
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)

    def __str__(self):
        return self.id_question + ' - ' + self.choice

class Answer(models.Model):
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    id_student = models.ForeignKey(PaeUser, null=True, on_delete=models.SET_NULL, related_name='student_answer')
    id_tutor = models.ForeignKey(PaeUser, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField()
    answer = models.JSONField()

    def __str__(self):
        return self.id_question + ' - ' + self.id_student + ' - ' + self.id_tutor + ' - ' + self.date + ' ' + self.answer

class Session(models.Model):
    id_subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    date = models.DateTimeField()
    id_tutor = models.ForeignKey(PaeUser, null=True, on_delete=models.SET_NULL)
    id_student = models.ForeignKey(PaeUser, null=True, on_delete=models.SET_NULL, related_name='session_student')
    file = models.FileField(null=True)
    status = models.IntegerField()
    spot = models.CharField(max_length=50, null=True)
    request_time = models.DateTimeField()
    verify_time = models.DateTimeField(null=True)
    id_admin_verify = models.ForeignKey(PaeUser, null=True, on_delete=models.SET_NULL, related_name='id_admin_verify')

    def __str__(self):
        return self.id_subject + ' - ' + self.date + ' - ' + self.id_tutor + ' - ' + self.id_student + ' - ' + self.status




