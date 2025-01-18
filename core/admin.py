from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import ArrayWidget, WysiwygWidget
from .models import (
    Assignment,
    Report,
    Testimonial,
    TeamMember,
    Banner,
    PhotoGallery,
    Photo,
    ContactInformation
)

from django.contrib.auth.models import Group

admin.site.unregister(Group)

@admin.register(Assignment)
class AssignmentAdmin(ModelAdmin):
    list_display = ('title', 'duration', 'created_at')
    search_fields = ('title', 'description')
    formfield_overrides = {
        'description': {'widget': WysiwygWidget},
    }

@admin.register(Report)
class ReportAdmin(ModelAdmin):
    list_display = ('client', 'service_type', 'created_at')
    list_filter = ('service_type', 'created_at')
    search_fields = ('client', 'description')
    formfield_overrides = {
        'description': {'widget': WysiwygWidget},
        'practice_areas': {'widget': WysiwygWidget},
        'contracts': {'widget': WysiwygWidget},
    }

@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ('name', 'company', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('name', 'company', 'content')
    formfield_overrides = {
        'content': {'widget': WysiwygWidget},
    }

@admin.register(TeamMember)
class TeamMemberAdmin(ModelAdmin):
    list_display = ('name', 'position', 'email', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'position', 'bio')
    formfield_overrides = {
        'bio': {'widget': WysiwygWidget},
    }

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1
    fields = ('image', 'caption', 'order')

@admin.register(PhotoGallery)
class PhotoGalleryAdmin(ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    inlines = [PhotoInline]
    formfield_overrides = {
        'description': {'widget': WysiwygWidget},
    }

@admin.register(Banner)
class BannerAdmin(ModelAdmin):
    list_display = ('title', 'active', 'order')
    list_editable = ('active', 'order')
    list_filter = ('active',)
    search_fields = ('title', 'subtitle')

@admin.register(ContactInformation)
class ContactInformationAdmin(ModelAdmin):
    list_display = ('email', 'phone')
    formfield_overrides = {
        'office_hours': {'widget': WysiwygWidget},
        'google_maps_embed': {'widget': WysiwygWidget},
    }

    def has_add_permission(self, request):
        # Check if there's already a ContactInformation instance
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

# Optional: Register Photo model separately if you want to manage photos independently
@admin.register(Photo)
class PhotoAdmin(ModelAdmin):
    list_display = ('gallery', 'caption', 'order')
    list_filter = ('gallery',)
    list_editable = ('order',)
    search_fields = ('caption',)