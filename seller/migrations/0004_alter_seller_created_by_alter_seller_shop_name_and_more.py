# Generated by Django 4.0.4 on 2022-06-07 04:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seller', '0003_alter_seller_created_by_alter_seller_updated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='created_by',
            field=models.ForeignKey(max_length=1, on_delete=django.db.models.deletion.CASCADE, related_name='creater_seller', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='seller',
            name='shop_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='seller',
            name='updated_by',
            field=models.ForeignKey(max_length=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updater_seller', to=settings.AUTH_USER_MODEL),
        ),
    ]
