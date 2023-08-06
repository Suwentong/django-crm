# Generated by Django 4.2.4 on 2023-08-05 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='state',
        ),
        migrations.RemoveField(
            model_name='record',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='record',
            name='patronymic',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='record',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='responsilbe_person',
            field=models.CharField(max_length=50, null=True),
        ),
    ]