# Generated by Django 4.2.2 on 2023-06-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_buyer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='propic',
            field=models.FileField(default='anonymous.jpg', upload_to='media/'),
        ),
    ]
