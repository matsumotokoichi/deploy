# Generated by Django 5.0.1 on 2024-03-18 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_institution_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='institution_name',
            field=models.CharField(max_length=50),
        ),
    ]
