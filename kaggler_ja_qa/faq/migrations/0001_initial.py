# Generated by Django 3.0.4 on 2020-03-14 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_text', models.TextField()),
                ('q_posted_at', models.DateTimeField(auto_now_add=True)),
                ('a_text', models.TextField()),
                ('a_posted_at', models.DateTimeField(auto_now_add=True)),
                ('label', models.CharField(choices=[('preprocessing', '前処理'), ('feature_engineering', '特徴量エンジニアリング'), ('modeling', 'モデリング')], default='preprocessing', max_length=32)),
                ('a_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='faq.User')),
                ('q_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='faq.User')),
            ],
        ),
    ]
