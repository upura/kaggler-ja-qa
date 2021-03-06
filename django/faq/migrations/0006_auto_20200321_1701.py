# Generated by Django 3.0.4 on 2020-03-21 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0005_auto_20200321_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionanswer',
            name='label',
            field=models.CharField(choices=[('探索的データ分析', '探索的データ分析'), ('特徴量エンジニアリング', '特徴量エンジニアリング'), ('モデリング', 'モデリング'), ('検証', '検証'), ('アンサンブル', 'アンサンブル'), ('その他', 'その他')], default='その他', max_length=32),
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='q_posted_at',
            field=models.DateField(),
        ),
    ]
