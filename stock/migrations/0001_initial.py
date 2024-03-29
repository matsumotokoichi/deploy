# Generated by Django 5.0.1 on 2024-03-01 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_alter_institutioncode_institution_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('category', models.CharField(choices=[('1', '慢性疾患'), ('2', '感冒薬'), ('3', '抗アレルギー薬'), ('4', 'その他')], max_length=50)),
                ('stock', models.CharField(max_length=100)),
                ('memo', models.TextField()),
                ('create_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('institution_code_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.institutioncode')),
            ],
            options={
                'db_table': 'medicine',
            },
        ),
    ]
