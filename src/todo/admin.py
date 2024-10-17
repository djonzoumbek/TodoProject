from django.contrib import admin
from .models import TodoList, Todo



class TodoInline(admin.TabularInline): #cette classe permet d'afficher liés à une todo liste
    model = Todo
    extra = 0

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    inlines = (TodoInline,)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'completed', 'favorite')
