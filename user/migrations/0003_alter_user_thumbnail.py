# Generated by Django 4.2 on 2023-05-19 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='thumbnail',
            field=models.CharField(blank=True, default='default_profile.png', max_length=256, null=True),
        ),
    ]
