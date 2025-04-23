from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'custom_choices')  # Customize admin list display
    search_fields = ('title', 'user__username')  # Enable search by title and username
    list_filter = ('created_at', 'custom_choices')  # Add filter options
    ordering = ('-created_at',)  # Show latest blogs first
    prepopulated_fields = {'title': ('title',)}  # Auto-generate slug (optional)

