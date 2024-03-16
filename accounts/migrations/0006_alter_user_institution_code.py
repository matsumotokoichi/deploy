# Generated by Django 5.0.1 on 2024-03-16 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_institution_name_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='institution_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.institutioncode'),
        ),
    ]
