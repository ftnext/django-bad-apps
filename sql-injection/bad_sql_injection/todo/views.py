from django.shortcuts import render

from .models import Todo


def todo_list(request):
    if "todo" not in request.GET:
        todos = Todo.objects.all()
    else:
        todo_str = request.GET["todo"]
        sql = (
            "SELECT id, id_str, todo, created_date, due_date FROM todos "
            "WHERE todo = '{}';".format(todo_str)
        )
        todos = Todo.objects.raw(sql)
    return render(request, "todo/list.html", {"todos": todos})
