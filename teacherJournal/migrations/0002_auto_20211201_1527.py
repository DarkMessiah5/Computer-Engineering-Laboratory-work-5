# Generated by Django 3.2.9 on 2021-12-01 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacherJournal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='student',
        ),
        migrations.AddField(
            model_name='student',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='teacherJournal.subject'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default='', max_length=127),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(default='', max_length=127),
        ),
    ]
