# Generated by Django 3.1 on 2021-01-16 05:03


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20210111_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='banner_image',
            field=models.ImageField(default='default_profile-bg.jpg', upload_to='profile_background_pics'),
        ),
    ]
