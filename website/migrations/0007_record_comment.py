# Generated by Django 4.2.4 on 2023-08-05 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_rename_responsilbe_person_record_responsible_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='comment',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
