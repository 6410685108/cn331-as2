# Generated by Django 4.2.5 on 2023-09-24 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='remaining_class',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
