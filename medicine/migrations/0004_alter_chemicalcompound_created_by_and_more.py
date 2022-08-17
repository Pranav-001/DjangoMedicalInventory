# Generated by Django 4.0.4 on 2022-06-07 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicine', '0003_alter_medicine_created_by_alter_medicine_updated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemicalcompound',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='creater_Chemical', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chemicalcompound',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='updater_Chemical', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='creater_medicine', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='updater_medicine', to=settings.AUTH_USER_MODEL),
        ),
    ]