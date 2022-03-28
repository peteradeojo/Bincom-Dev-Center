from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from .models import Todo


def index(request):
    list = Todo.objects.all().order_by('status', '-time')
    return render(request, 'index.html', {
        'todo_list': list,
    })


def toggle(request, id):
    item = Todo.objects.get(id=id)
    item.toggle()
    item.save()
    return HttpResponseRedirect('/')


def delete(request, id):
    # item = Todo.objects.get(id=id)
    Todo.objects.get(id=id).delete()
    return HttpResponseRedirect('/')

def new(request):
  # pass
  title, description = request.POST['title'], request.POST['description']
  item = Todo()
  item.title = title
  item.description = description
  item.save()
  return HttpResponseRedirect('/')
