# Generated by Django 4.2.6 on 2023-10-07 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_subject_remaining_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='is_open',
            field=models.BooleanField(default=False),
        ),
    ]
