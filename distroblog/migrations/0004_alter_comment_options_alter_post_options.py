# Generated by Django 4.2.9 on 2024-02-22 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distroblog', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
    ]