# Generated by Django 3.1 on 2022-01-16 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_video',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
