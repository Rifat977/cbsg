from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from .models import *
from django.contrib.auth.models import Group

# Unregister the default Group model
admin.site.unregister(Group)

# -------------------------- HOME -------------------------- #
@admin.register(HomeBanner)
class HomeBannerAdmin(ModelAdmin):
    list_display = ('id', 'image')
    search_fields = ('id',)

@admin.register(RecentProject)
class RecentProjectAdmin(ModelAdmin):
    list_display = ('assignment_name', 'contract_duration', 'contract_with')
    search_fields = ('assignment_name', 'contract_with')

    formfield_overrides = {
        models.TextField: {'widget': WysiwygWidget()},
    }

@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ('name', 'title', 'organization')
    search_fields = ('name', 'organization')

    formfield_overrides = {
        models.TextField: {'widget': WysiwygWidget()},
    }

@admin.register(WorkLocation)
class WorkLocationAdmin(ModelAdmin):
    list_display = ('country', 'work_description')
    search_fields = ('country',)

    formfield_overrides = {
        models.TextField: {'widget': WysiwygWidget()},
    }

# -------------------------- ABOUT US -------------------------- #
@admin.register(CoreCompetency)
class CoreCompetencyAdmin(ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

    formfield_overrides = {
        models.TextField: {'widget': WysiwygWidget()},
    }

@admin.register(About)
class AboutAdmin(ModelAdmin):
    list_display = ('company_name', 'partnership_area')
    search_fields = ('company_name',)

    formfield_overrides = {
        models.TextField: {'widget': WysiwygWidget()},
    }

# -------------------------- OUR SERVICES -------------------------- #
@admin.register(SubArea)
class SubAreaAdmin(ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

    formfield_overrides = {
        models.TextField: {'widget': WysiwygWidget()},
    }

@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ('intro_text',)
    search_fields = ('intro_text',)

    formfield_overrides = {
        models.TextField: {'widget': WysiwygWidget()},
    }

# -------------------------- PRACTICE AREAS -------------------------- #
@admin.register(PracticeArea)
class PracticeAreaAdmin(ModelAdmin):
    list_display = ('name', 'introduction')
    search_fields = ('name',)

    formfield_overrides = {
        models.TextField: {'widget': WysiwygWidget()},
    }

@admin.register(MilestoneWork)
class MilestoneWorkAdmin(ModelAdmin):
    list_display = ('practice_area', 'description')
    search_fields = ('practice_area__name',)

    formfield_overrides = {
        models.TextField: {'widget': WysiwygWidget()},
    }

# -------------------------- OUR TEAM -------------------------- #
@admin.register(TeamMember)
class TeamMemberAdmin(ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category')

# -------------------------- OUR WORK & REACH -------------------------- #
@admin.register(Assignment)
class AssignmentAdmin(ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

    formfield_overrides = {
        models.TextField: {'widget': WysiwygWidget()},
    }

@admin.register(WorkReach)
class WorkReachAdmin(ModelAdmin):
    list_display = ('country', 'assignment_name')
    search_fields = ('country', 'assignment_name')

    formfield_overrides = {
        models.TextField: {'widget': WysiwygWidget()},
    }

# -------------------------- OUR PRODUCTS -------------------------- #
@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('report_name',)
    search_fields = ('report_name',)

    formfield_overrides = {
        models.TextField: {'widget': WysiwygWidget()},
    }

# -------------------------- REQUEST FORM -------------------------- #
@admin.register(RequestForm)
class RequestFormAdmin(ModelAdmin):
    list_display = ('name', 'email', 'product')
    search_fields = ('name', 'email', 'product__report_name')

# -------------------------- PHOTO GALLERY -------------------------- #
@admin.register(PhotoGallery)
class PhotoGalleryAdmin(ModelAdmin):
    list_display = ('caption',)
    search_fields = ('caption',)

# -------------------------- CONTACT -------------------------- #
@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ('location_name', 'address', 'phone', 'email')
    search_fields = ('location_name', 'address', 'phone', 'email')
