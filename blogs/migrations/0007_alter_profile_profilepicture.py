# Generated by Django 4.0.3 on 2022-04-04 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_alter_profile_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilePicture',
            field=models.ImageField(blank=True, null=True, upload_to='C:\\Users\\forty\\OneDrive\\Documents\\GitHub\\Fortyseven-Django\\staticfiles/img/blog-assests/profile-pictures/'),
        ),
    ]