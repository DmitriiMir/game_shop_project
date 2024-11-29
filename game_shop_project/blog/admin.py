from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Отображаемые поля
    search_fields = ('title',)  # Поиск по названию
    list_filter = ('created_at',)  # Фильтр по дате создания

