# Generated by Django 5.0.6 on 2024-07-16 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_remove_skill_proficiency_skill_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='icon',
            field=models.ImageField(default='icons/default_icon.png', upload_to='icons/'),
        ),
    ]
