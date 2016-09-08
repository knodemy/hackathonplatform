from django.contrib import admin
from django.contrib.admin import AdminSite
#from .models import Author
from .models import Event, Program_Flow
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


'''
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
    
    
'''
class EventAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'added_by', None) is None:
            obj.added_by = request.user
        obj.last_modified_by = request.user
        obj.save()
        
    def get_queryset(self, request):
        qs = super(EventAdmin, self).get_queryset(request)
        #qs = self.get_queryset(request)

        # If super-user, show all comments
        if request.user.is_superuser:
            return qs
        
        return qs.filter(added_by=request.user)
        
    '''
    def change_view(self, request, object_id, extra_context=None):
        result = super(EventAdmin, self).change_view(request, object_id, extra_context)
        event = Event.objects.get(id__exact=object_id)
        if not request.POST.has_key('_addanother') and not request.POST.has_key('_continue'):
            result['Location'] = event.get_absolute_url()
        return result
    '''
    '''  

        qs = self.get_queryset(request)
        
        list_display = []
        for x in qs:
            list_display.append(x)
    
        return list_display
    '''

class EventAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'added_by', None) is None:
            obj.added_by = request.user
        obj.last_modified_by = request.user
        obj.save()
        
    def get_queryset(self, request):
        qs = super(EventAdmin, self).get_queryset(request)
        #qs = self.get_queryset(request)

        # If super-user, show all comments
        if request.user.is_superuser:
            return qs
        
        return qs.filter(added_by=request.user)


admin.site.register(Event, EventAdmin)
admin.site.register(Program_Flow)
admin.site.site_header = 'knodemy Hackathon Platform'
admin.site.site_title = "knodemy"

