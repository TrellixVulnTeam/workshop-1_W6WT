# Generated by Django 3.1.5 on 2021-02-08 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RiseApp_Projects', '0006_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='RiseApp_Projects.project'),
        ),
    ]