from django.contrib import admin
from .models import (
    bangla_newspaper,
    english_newspaper,
    job_website,
    magazines,
    indian_bangla_newspaper,
    news_channel,
    note
)

# Register your models here.
admin.site.site_header = 'Online NEWS'

admin.site.register(bangla_newspaper)
admin.site.register(english_newspaper)
admin.site.register(job_website)
admin.site.register(magazines)
admin.site.register(indian_bangla_newspaper)
admin.site.register(news_channel)
admin.site.register(note)