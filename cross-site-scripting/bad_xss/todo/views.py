from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import Todo


@login_required
def todo_list(request):
    todos = Todo.objects.all()
    todo_rows = "\n".join(
        f"""
<tr>
    <td>{todo.id_str}</td>
    <td>{todo.todo}</td>
    <td>{todo.created_date}</td>
    <td>{todo.due_date}</td>
</tr>"""
        for todo in todos
    )

    html = f"""\
<h1>Bad Todo List</h1>
<a href="/todolist/new/">作成</a>
<table>
    <tr>
        <td>ID</td>
        <td>todo</td>
        <td>登録日</td>
        <td>期限</td>
    </tr>
{todo_rows}
</table>"""
    return HttpResponse(html)


@login_required
def create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            _ = form.save()
            return redirect("create_todo")
    else:
        form = TodoForm()
    return render(request, "todo/create.html", {"form": form})
