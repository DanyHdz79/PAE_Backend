from django.db import models

# Create your models here.
class Admin(models.Model):
    id = models.EmailField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=256) #ecrypt password

    def __str__(self):
        return self.id + ' ' + self.name

class Career(models.Model):
    id = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.id

class Survey(models.Model):
    creation_date = models.DateTimeField()
    survey_type = models.IntegerField()

class User(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=256)
    semester = models.IntegerField()
    career = models.ForeignKey(Career, on_delete=models.RESTRICT)
    user_type = models.IntegerField()
    status = models.IntegerField()

    def __str__(self):
        return self.id + ' - ' + str(self.user_type)

class Subject(models.Model):
    class Meta:
        unique_together = (('id', 'id_career'),)

    id_subject = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    id_career = models.ForeignKey(Career, on_delete=models.RESTRICT)
    semester = models.IntegerField()
    tutors = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.id_subject + ' - ' + self.name + ' - ' + str(self.id_career)


class Schedule(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    day_hour = models.CharField(max_length=4)

    def __str__(self):
        return self.id_user + ' ' + self.day_hour

class Question(models.Model):
    id_survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    question_type = models.IntegerField()

    def __str__(self):
        return self.id_survey + ' - ' + self.question + ' - ' +self.question_type

class Answer(models.Model):
    id_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    id_student = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='student_answer')
    id_tutor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField()
    answer = models.JSONField()

    def __str__(self):
        return self.id_question + ' - ' + self.id_student + ' - ' + self.id_tutor + ' - ' + self.date + ' ' + self.answer

class Session(models.Model):
    id_subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    description = models.TextField()
    date = models.DateTimeField()
    id_tutor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    id_student = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='session_student')
    file = models.FileField(null=True)
    status = models.IntegerField()
    spot = models.CharField(max_length=50, null=True)
    request_time = models.DateTimeField()
    verify_time = models.DateTimeField(null=True)
    id_admin_verify = models.ForeignKey(Admin, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.id_subject + ' - ' + self.date + ' - ' + self.id_tutor + ' - ' + self.id_student + ' - ' + self.status




