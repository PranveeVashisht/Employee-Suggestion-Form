from django.contrib import admin
from .models import Suggestion

# Register your models here.
@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display= ['content','created_at','name','email']
    list_filter= ['name']
    search_fields = ['name','content']
