from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import *


class StudentAdmin(admin.ModelAdmin):
    # Define which fields you want to display in the list view
    list_display = ('student_id', 'name', 'email', 'phone', 'age', 'department')

    # Optionally, you can add filters and search capabilities
    list_filter = ('department', 'age')
    search_fields = ('name', 'student_id', 'email')
    ordering = ('-age',)

class RecipeAdmin(admin.ModelAdmin):
    # Define the fields to display in the list view
    list_display = ('recipe_name', 'user', 'recipe_view_count', 'recipe_image')

    # Add filters and search capabilities if needed
    list_filter = ('user', 'recipe_view_count')
    search_fields = ('recipe_name', 'recipe_descrition')

    # Optionally, add the ability to edit fields inline
    fields = ('user', 'recipe_name', 'recipe_descrition', 'recipe_image', 'recipe_view_count')
    readonly_fields = ('recipe_view_count',)  # Make recipe_view_count read-only

    # Add a method to display a thumbnail of the image in the list view
    def recipe_image(self, obj):
        if obj.recipe_image:
            return format_html('<img src="{}" width="100" height="100"/>', f"/media/{obj.recipe_image.url}")
        return 'No Image'
    recipe_image.allow_tags = True
    recipe_image.short_description = 'Image Thumbnail'

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(StudentID)
admin.site.register(Student, StudentAdmin)
admin.site.register(Department)
