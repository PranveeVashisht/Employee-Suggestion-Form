# Generated by Django 4.2.2 on 2023-06-19 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('suggestions', '0002_suggestion_email_suggestion_name_suggestion_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
