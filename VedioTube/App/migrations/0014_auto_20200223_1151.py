# Generated by Django 3.0.3 on 2020-02-23 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_videos_data_dislikes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos_data',
            name='Comments',
            field=models.CharField(default='', max_length=1000),
        ),
    ]