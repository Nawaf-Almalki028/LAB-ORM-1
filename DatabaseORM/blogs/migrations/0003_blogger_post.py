# Generated by Django 5.2.4 on 2025-07-14 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_blogger_is_published_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogger',
            name='post',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
