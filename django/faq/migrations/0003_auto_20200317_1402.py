# Generated by Django 3.0.4 on 2020-03-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_questionanswer_slack_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionanswer',
            name='a_author',
        ),
        migrations.RemoveField(
            model_name='questionanswer',
            name='a_posted_at',
        ),
        migrations.RemoveField(
            model_name='questionanswer',
            name='q_author',
        ),
        migrations.RemoveField(
            model_name='questionanswer',
            name='slack_url',
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='label',
            field=models.CharField(choices=[('前処理', '前処理'), ('特徴量エンジニアリング', '特徴量エンジニアリング'), ('モデリング', 'モデリング')], default='前処理', max_length=32),
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='q_posted_at',
            field=models.DateTimeField(),
        ),
    ]
