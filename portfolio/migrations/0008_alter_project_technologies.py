# Generated by Django 5.0.6 on 2024-07-16 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_project_technologies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=models.CharField(choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('Javascript', 'JavaScript'), ('React', 'React'), ('Node.js', 'Node.js'), ('Django', 'Django')], default='', max_length=50),
        ),
    ]
