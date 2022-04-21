# Generated by Django 4.0.3 on 2022-04-18 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
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
            name='User',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=256)),
                ('semester', models.IntegerField()),
                ('user_type', models.IntegerField()),
                ('status', models.IntegerField()),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='sistema_pae.career')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_subject', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('semester', models.IntegerField()),
                ('id_career', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='sistema_pae.career')),
                ('tutors', models.ManyToManyField(to='sistema_pae.user')),
            ],
            options={
                'unique_together': {('id', 'id_career')},
            },
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
                ('id_admin_verify', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema_pae.admin')),
                ('id_student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='session_student', to='sistema_pae.user')),
                ('id_subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema_pae.subject')),
                ('id_tutor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema_pae.user')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_hour', models.CharField(max_length=4)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema_pae.user')),
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
                ('id_student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_answer', to='sistema_pae.user')),
                ('id_tutor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sistema_pae.user')),
            ],
        ),
    ]
