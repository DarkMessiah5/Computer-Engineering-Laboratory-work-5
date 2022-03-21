# Generated by Django 3.2.9 on 2021-12-01 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('mark', models.IntegerField(choices=[(2, 2), (3, 3), (4, 4), (5, 5)])),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacherJournal.student')),
            ],
        ),
    ]