# Generated by Django 4.2.4 on 2023-08-05 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_record_state_remove_record_zipcode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
