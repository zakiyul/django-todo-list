from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(req):
    if req.method == 'POST':
        task = req.POST['task']

        data = Todo()
        data.task = task
        data.save()
        return redirect('/')

    datas = Todo.objects.all()
    return render(req, 'index.html',{
        'datas':datas
    })

def delete(req, pk):
    if req.method == 'POST':

        data = Todo.objects.get(id=pk)
        data.delete()
        return redirect('/')

    return render(req, 'delete.html')

