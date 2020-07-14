from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from .models import Todo


# Create your views here.

def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, "todoapp/index.html", {
        "todo_items": todo_items
    })


def add_todo(request):
    time = timezone.now()
    content = request.POST["content"]
    Todo.objects.create(added_date=time, text=content)

    return HttpResponseRedirect(reverse('index'))


def delete_todo(request, todo_id):
    Todo.objects.get(pk=todo_id).delete()
    return HttpResponseRedirect(reverse("index"))
