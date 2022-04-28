# Generated by Django 4.0.3 on 2022-04-28 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PaeUser',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('semester', models.IntegerField()),
                ('user_type', models.IntegerField()),
                ('status', models.IntegerField()),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='sistema_pae.career')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('semester', models.IntegerField()),
                ('id_career', models.ManyToManyField(to='sistema_pae.career')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField()),
                ('survey_type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TutorSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pae.subject')),
                ('id_tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pae.paeuser')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('file', models.FileField(null=True, upload_to='')),
                ('status', models.IntegerField()),
                ('spot', models.CharField(max_length=50, null=True)),
                ('request_time', models.DateTimeField()),
                ('verify_time', models.DateTimeField(null=True)),
                ('id_admin_verify', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='id_admin_verify', to='sistema_pae.paeuser')),
                ('id_student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='session_student', to='sistema_pae.paeuser')),
                ('id_subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema_pae.subject')),
                ('id_tutor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema_pae.paeuser')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_hour', models.CharField(max_length=4)),
                ('available', models.BooleanField(default=True)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pae.paeuser')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('question_type', models.IntegerField()),
                ('id_survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pae.survey')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('answer', models.JSONField()),
                ('id_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pae.question')),
                ('id_student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_answer', to='sistema_pae.paeuser')),
                ('id_tutor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema_pae.paeuser')),
            ],
        ),
    ]
