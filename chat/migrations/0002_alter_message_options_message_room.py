# Generated by Django 5.1.4 on 2025-01-09 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['timestamp']},
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.CharField(default='general', max_length=255),
        ),
    ]
