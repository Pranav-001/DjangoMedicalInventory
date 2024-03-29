# Generated by Django 4.0.4 on 2022-06-07 03:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='created_by',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.DO_NOTHING, related_name='creater', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='company',
            name='updated_by',
            field=models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='updater', to=settings.AUTH_USER_MODEL),
        ),
    ]
