from django.contrib import admin
from .models import Tournament, WebUser, New
from django_summernote.admin import SummernoteModelAdmin
#Add Summernote to admin panel


@admin.register(Tournament)
class TournamentAdmin(SummernoteModelAdmin):

    list_display = ('name', 'category')
    search_fields = ['name', 'category', 'description',]
    list_filter = ('category','created_on',)
    summernote_fields = ('description',)

@admin.register(New)
class NewAdmin(SummernoteModelAdmin):

    list_display = ('title',)
    search_fields = ['title', 'content',]
    list_filter = ('created_on', 'status')
    summernote_fields = ('content',)
# Register your models here.

admin.site.register(WebUser)