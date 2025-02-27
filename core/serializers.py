# serializers.py

from rest_framework import serializers
from .models import *

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

class WorkLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkLocation
        fields = '__all__'


# serializers.py (continued)

class CoreCompetencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreCompetency
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):
    core_competencies = CoreCompetencySerializer(many=True)

    class Meta:
        model = About
        fields = '__all__'

# serializers.py (continued)

class SubAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubArea
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    sub_areas = SubAreaSerializer(many=True)

    class Meta:
        model = Service
        fields = '__all__'

# serializers.py (continued)

class PracticeAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeArea
        fields = '__all__'

class MilestoneWorkSerializer(serializers.ModelSerializer):
    practice_area = PracticeAreaSerializer()

    class Meta:
        model = MilestoneWork
        fields = '__all__'

# serializers.py (continued)

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'

# serializers.py (continued)

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class WorkReachSerializer(serializers.ModelSerializer):
    highlight_assignments = AssignmentSerializer(many=True)

    class Meta:
        model = WorkReach
        fields = '__all__'

# serializers.py (continued)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# serializers.py (continued)

class RequestFormSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = RequestForm
        fields = '__all__'

# serializers.py (continued)

class PhotoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGallery
        fields = '__all__'

# serializers.py (continued)

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
