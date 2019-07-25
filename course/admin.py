from django.contrib import admin
from course.models import Courses, Review

# Register your models here.

# Course Admin
class CoursesAdmin(admin.ModelAdmin):
    # readonly_fields = ('creado','editado')
    list_display = ('title', 'url')

# Review Admin
class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', )
    list_display = ('course', 'name', 'email', 'comment', 'rating', 'created_at')

    def course(self, obj):
        return ', '.join([c.nombre for c in obj.course.all().order_by('title')])
    course.short_description = 'reviews'


admin.site.register(Courses, CoursesAdmin)
admin.site.register(Review, ReviewAdmin)