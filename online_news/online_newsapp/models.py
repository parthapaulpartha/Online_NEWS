from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class bangla_newspaper(models.Model):
    name = models.CharField(max_length=50, default='')
    link = models.URLField(max_length=200, default='')
    image = models.ImageField(upload_to='b_news', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Bangla Newspaper'

class english_newspaper(models.Model):
    name = models.CharField(max_length=50, default='')
    link = models.URLField(max_length=200, default='')
    image = models.ImageField(upload_to='e_news', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'English Newspaper'

class job_website(models.Model):
    name = models.CharField(max_length=50, default='')
    link = models.URLField(max_length=200, default='')
    image = models.ImageField(upload_to='job_site', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Job Websites'

class magazines(models.Model):
    name = models.CharField(max_length=50, default='')
    link = models.URLField(max_length=200, default='')
    image = models.ImageField(upload_to='magazines', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Magazines'

class indian_bangla_newspaper(models.Model):
    name = models.CharField(max_length=50, default='')
    link = models.URLField(max_length=200, default='')
    image = models.ImageField(upload_to='i_b_news', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Indian Bangla Newspaper'

class news_channel(models.Model):
    name = models.CharField(max_length=50, default='')
    link = models.URLField(max_length=200, default='')
    image = models.ImageField(upload_to='news_channel', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'News Channel'

class note(models.Model):
    name = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    note_text = models.TextField(max_length=900, default='')
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = ' Note '