# Generated by Django 3.1.7 on 2021-02-27 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('location', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('is_liked', models.CharField(max_length=200)),
            ],
        ),
    ]
