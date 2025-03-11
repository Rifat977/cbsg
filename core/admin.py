from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from .models import *
from django.contrib.auth.models import Group

# Unregister the default Group model
admin.site.unregister(Group)

@admin.register(CompanyProfile)
class CompanyProfileAdmin(ModelAdmin):
    list_display = ('contracts_international_agencies', 'us_government_project', 'years_of_experience')
    search_fields = ('about_text', 'od_text')
    formfield_overrides = {models.TextField: {'widget': WysiwygWidget()}}

@admin.register(HomeBanner)
class HomeBannerAdmin(ModelAdmin):
    list_display = ('caption',)
    search_fields = ('caption',)

@admin.register(RecentProject)
class RecentProjectAdmin(ModelAdmin):
    list_display = ('assignment_name', 'assignment_start', 'assignment_end', 'assignment_with')
    search_fields = ('assignment_name', 'assignment_with')
    formfield_overrides = {models.TextField: {'widget': WysiwygWidget()}}

@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ('name', 'title', 'organization')
    search_fields = ('name', 'organization')
    formfield_overrides = {models.TextField: {'widget': WysiwygWidget()}}

@admin.register(CoreCompetency)
class CoreCompetencyAdmin(ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    formfield_overrides = {models.TextField: {'widget': WysiwygWidget()}}

@admin.register(About)
class AboutAdmin(ModelAdmin):
    list_display = ('company_name',)
    search_fields = ('company_name', 'about_text')
    formfield_overrides = {models.TextField: {'widget': WysiwygWidget()}}

@admin.register(YearRange)
class YearRangeAdmin(ModelAdmin):
    list_display = ('year_range',)
    search_fields = ('year_range',)

@admin.register(HistoryTimeline)
class HistoryTimelineAdmin(ModelAdmin):
    list_display = ('year_range', 'title')
    search_fields = ('title', 'year_range__year_range')
    formfield_overrides = {models.TextField: {'widget': WysiwygWidget()}}

@admin.register(StrategicPartner)
class StrategicPartnerAdmin(ModelAdmin):
    list_display = ('company_name', 'company_website_link')
    search_fields = ('company_name',)

@admin.register(SubArea)
class SubAreaAdmin(ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    formfield_overrides = {models.TextField: {'widget': WysiwygWidget()}}




from django import forms



class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['sub_area', 'service_type', 'sub_service', 'practice_area', 'title', 'photo', 'description', 'company_logo']  # Include all fields

@admin.register(Assignment)
class AssignmentAdmin(ModelAdmin):
    form = AssignmentForm

    class Media:
        js = ('assignment.js',)  # Include your custom JavaScript file

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    list_display = ('title', 'service_type', 'sub_service', 'practice_area')
    search_fields = ('title', 'practice_area')
    formfield_overrides = {models.TextField: {'widget': WysiwygWidget()}}




# @admin.register(Assignment)
# class AssignmentAdmin(ModelAdmin):
#     list_display = ('title', 'service_type', 'sub_service', 'practice_area')
#     search_fields = ('title', 'practice_area')
#     formfield_overrides = {models.TextField: {'widget': WysiwygWidget()}}

@admin.register(ServiceIntro)
class ServiceIntroAdmin(ModelAdmin):
    list_display = ('intro_text',)
    search_fields = ('intro_text',)
    formfield_overrides = {models.TextField: {'widget': WysiwygWidget()}}

@admin.register(PracticeArea)
class PracticeAreaAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    formfield_overrides = {models.TextField: {'widget': WysiwygWidget()}}

@admin.register(TeamMember)
class TeamMemberAdmin(ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category')
    formfield_overrides = {models.TextField: {'widget': WysiwygWidget()}}

@admin.register(MilestoneWork)
class MilestoneWorkAdmin(ModelAdmin):
    list_display = ('practice_area',)
    search_fields = ('practice_area__name',)
    formfield_overrides = {models.TextField: {'widget': WysiwygWidget()}}

@admin.register(WorkLocation)
class WorkLocationAdmin(ModelAdmin):
    list_display = ('country', 'subcontinent')
    search_fields = ('country', 'subcontinent')
    formfield_overrides = {models.TextField: {'widget': WysiwygWidget()}}

@admin.register(RequestForm)
class RequestFormAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')
    formfield_overrides = {models.TextField: {'widget': WysiwygWidget()}}

@admin.register(PhotoGallery)
class PhotoGalleryAdmin(ModelAdmin):
    list_display = ('caption',)
    search_fields = ('caption',)

@admin.register(ContactDetail)
class ContactDetailAdmin(ModelAdmin):
    list_display = ('name', 'organization', 'email', 'cell')
    search_fields = ('name', 'organization', 'email')