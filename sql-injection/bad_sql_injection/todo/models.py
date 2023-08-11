from django.db import models
from django.utils import timezone


class Todo(models.Model):
    id_str = models.CharField("ID", max_length=20)
    todo = models.CharField("todo", max_length=100)
    created_date = models.DateTimeField("登録日", default=timezone.now)
    due_date = models.DateField("期限", blank=False, null=False)

    class Meta:
        db_table = "todos"
