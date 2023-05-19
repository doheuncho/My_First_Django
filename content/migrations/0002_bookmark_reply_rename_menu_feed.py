# Generated by Django 4.2 on 2023-05-19 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_id', models.IntegerField(default=0)),
                ('user_id', models.TextField(default='')),
                ('is_marked', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_id', models.IntegerField(default=0)),
                ('user_id', models.TextField(default='')),
                ('reply_content', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Menu',
            new_name='Feed',
        ),
    ]
