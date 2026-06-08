from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ToDoList
from .forms import ToDoListForm

# Create your views here.
def index(request):
    todolist_data = ToDoList.objects.all()
    
    return render(request, "index.html", {"todolist": todolist_data})


def create(request):
    if request.method == "POST":

        form = ToDoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            return render(request, "create.html", {"form": form})
    else:
        form = ToDoListForm()
        return render(request, "create.html", {"form": form})



def edit(request, pk):
    todo = get_object_or_404(ToDoList, pk=pk)

    if request.method == "POST":
        form = ToDoListForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            form = ToDoListForm(instance=todo)

    else:
        form = ToDoListForm(instance=todo)

    return render(request, "edit.html", {"form": form, "todo": todo})



def confirm_delete(request, pk):
    todo = get_object_or_404(ToDoList, pk=pk)
    if request.method == "POST":
        return render(request, "delete.html", {"pkk": pk, "todo": todo})


def delete(request, pk):
    todo = get_object_or_404(ToDoList, pk=pk)
    if request.method == "POST":
        todo.delete()
        return redirect("index")

    return render(request, "delete.html", {"todo": todo})
