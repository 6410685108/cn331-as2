# Generated by Django 4.2.5 on 2023-09-24 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_subject', models.IntegerField()),
                ('N_subject', models.CharField(max_length=64)),
                ('teacher', models.CharField(max_length=60)),
                ('max_class', models.IntegerField()),
            ],
        ),
    ]
