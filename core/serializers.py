from rest_framework import serializers, viewsets
from .models import *
# Serializers
class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = '__all__'

class HomeBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeBanner
        fields = '__all__'

class RecentProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentProject
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class CoreCompetencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreCompetency
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):
    core_competencies = CoreCompetencySerializer(many=True, read_only=True)
    
    class Meta:
        model = About
        fields = '__all__'
class YearRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearRange
        fields = '__all__'

class HistoryTimelineSerializer(serializers.ModelSerializer):
    year_range = YearRangeSerializer(read_only=True)

    class Meta:
        model = HistoryTimeline
        fields = '__all__'


class StrategicPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategicPartner
        fields = '__all__'

class SubServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubServiceArea
        fields = '__all__'



class ServiceIntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceIntro
        fields = '__all__'

class PracticeAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeArea
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    practice_area = PracticeAreaSerializer(read_only=True)
    sub_service_area = SubServiceAreaSerializer(read_only=True)

    class Meta:
        model = Assignment
        fields = '__all__'

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'

class MilestoneWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilestoneWork
        fields = '__all__'

class WorkLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkLocation
        fields = '__all__'

 
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'


class RequestFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestForm
        fields = '__all__'

class PhotoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGallery  # Fixed typo here
        fields = '__all__'