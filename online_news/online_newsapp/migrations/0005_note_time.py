# Generated by Django 3.0.3 on 2020-02-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_newsapp', '0004_indian_bangla_newspaper_news_channel_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
