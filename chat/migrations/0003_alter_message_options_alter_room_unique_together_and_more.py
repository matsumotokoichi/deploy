# Generated by Django 5.0.1 on 2024-03-16 07:37

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_message_create_at_alter_room_create_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('-create_at',)},
        ),
        migrations.AlterUniqueTogether(
            name='room',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='message',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 16, 16, 37, 30, 362847)),
        ),
        migrations.AlterField(
            model_name='room',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 16, 16, 37, 30, 362847)),
        ),
        migrations.AlterField(
            model_name='room',
            name='recipient_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipientcode', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='user_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usercode', to=settings.AUTH_USER_MODEL),
        ),
    ]