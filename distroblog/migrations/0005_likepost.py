# Generated by Django 4.2.9 on 2024-03-05 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distroblog', '0004_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]