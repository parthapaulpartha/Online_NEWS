from django.shortcuts import render, redirect
from .models import (
    bangla_newspaper,
    english_newspaper,
    job_website,
    magazines,
    indian_bangla_newspaper,
    news_channel,
    note,
)
from .forms import NoteForm

# Create your views here.
def home(request):
    job = job_website.objects.all()
    magazine = magazines.objects.all()
    i_b_news = indian_bangla_newspaper.objects.all()
    arg = {'job': job,
           'magazine': magazine,
           'i_b_news': i_b_news
           }
    return render(request, 'online_newsapp/home.html', arg)

def bangla_news(request):
    b_news = bangla_newspaper.objects.all()
    arg = {'b_news': b_news}
    return render(request, 'online_newsapp/bangla_newspaper.html', arg)

def english_news(request):
    e_news = english_newspaper.objects.all()
    arg = {'e_news': e_news}
    return render(request, 'online_newsapp/english_newspaper.html', arg)

def news_channels(request):
    n_channel = news_channel.objects.all()
    arg = {'n_channel': n_channel}
    return render(request, 'online_newsapp/news_channel.html', arg)

def notes(request):
    note_pad_all = note.objects.all()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = request.user
            instance.save()
            return redirect('/online_news/note')
    else:
        form = NoteForm()
        arg = {
            'form': form,
            'note_pad_all': note_pad_all
            }
    return render(request, 'online_newsapp/note.html', arg)