# Generated by Django 4.0.3 on 2022-03-29 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_blog_approved_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='approved_at',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]