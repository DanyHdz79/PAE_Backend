# Generated by Django 4.0.3 on 2022-04-28 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sistema_pae', '0005_rename_userpae_paeuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paeuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='paeuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
