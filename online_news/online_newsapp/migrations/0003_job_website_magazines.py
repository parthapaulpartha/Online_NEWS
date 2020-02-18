# Generated by Django 3.0.3 on 2020-02-14 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_newsapp', '0002_english_newspaper'),
    ]

    operations = [
        migrations.CreateModel(
            name='job_website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('link', models.URLField(default='')),
                ('image', models.ImageField(default='', upload_to='job_site')),
            ],
            options={
                'verbose_name_plural': 'Job Websites',
            },
        ),
        migrations.CreateModel(
            name='magazines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('link', models.URLField(default='')),
                ('image', models.ImageField(default='', upload_to='magazines')),
            ],
            options={
                'verbose_name_plural': 'Magazines',
            },
        ),
    ]
