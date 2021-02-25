# Generated by Django 3.1.2 on 2021-02-25 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LabExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateTimeField()),
                ('exam_name', models.CharField(max_length=20)),
                ('exam_description', models.CharField(max_length=500)),
                ('total_marks', models.FloatField()),
                ('pass_marks', models.FloatField()),
                ('exam_status', models.BooleanField()),
            ],
        ),
    ]