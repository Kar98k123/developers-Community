# Generated by Django 4.1.2 on 2022-11-22 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_review_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]
