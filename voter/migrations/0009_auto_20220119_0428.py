# Generated by Django 3.1 on 2022-01-19 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0008_auto_20220119_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('0', 'Select Gender')], default='0', max_length=10),
        ),
    ]