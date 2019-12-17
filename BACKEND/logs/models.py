from django.db import models
from django.conf import settings

# Create your models here.


class Log(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    commited_at = models.DateTimeField(auto_now=True)
    list_rate = models.IntegerField()

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return f'{self.user}({self.created_date})'


class TodoListTag(models.Model):
    content = models.CharField(max_length=100)


class TodoList(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE)
    tags = models.ManyToManyField(TodoListTag, related_name='tagged_lists')
    rate = models.IntegerField()


class TodoTag(models.Model):
    content = models.CharField(max_length=100)


class Todo(models.Model):
    checked = models.BooleanField(default=0)
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(
        TodoTag, related_name='tagged_todos')
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    # date = models.DateTimeField(auto_now_add=True)
    # labels = models.CharField(text_length=100)
