# Generated by Django 5.1.6 on 2025-03-13 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='users/default.png', null=True, upload_to='users/'),
        ),
    ]
