from django.contrib import admin
from app_manage.models import Project,Module
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'describe', 'create_time', 'update_time']  #显示字段
    search_fields = ['name']   # 搜索栏
    list_filter = ['status']   # 过滤器

class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'create_time', 'project']  #显示字段


admin.site.register(Project, ProjectAdmin)
admin.site.register(Module, ModuleAdmin)