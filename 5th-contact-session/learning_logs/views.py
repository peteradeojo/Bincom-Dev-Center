from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Entry, Topic
from .forms import EntryForm, TopicForm


# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')


@login_required
def topics(r):
    topics = Topic.objects.filter(owner=r.user).order_by('date_added')
    context = {'topics': topics}
    # pass
    return render(r, 'learning_logs/topics.html', context)


def topic(r, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != r.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(r, 'learning_logs/topic.html', context)


@login_required
def new_topic(r):
    if r.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=r.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.owner = r.user
            topic.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(r, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(r, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if r.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=r.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(r, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(r, entry_id):
    # pass
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != r.user:
        raise Http404

    if r.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=r.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(r, 'learning_logs/edit_entry.html', context)
