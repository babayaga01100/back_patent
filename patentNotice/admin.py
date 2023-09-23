from django.contrib import admin

from .models import PatentNotice

# Register your models here.
@admin.register(PatentNotice)
class PatentNoticeModelAdmin(admin.ModelAdmin):
    pass
