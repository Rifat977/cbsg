# views.py

from rest_framework import viewsets
from .models import *
from .serializers import *

# -------------------------- HOME -------------------------- #

class HomeBannerViewSet(viewsets.ModelViewSet):
    queryset = HomeBanner.objects.all()
    serializer_class = HomeBannerSerializer

class RecentProjectViewSet(viewsets.ModelViewSet):
    queryset = RecentProject.objects.all()
    serializer_class = RecentProjectSerializer

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class WorkLocationViewSet(viewsets.ModelViewSet):
    queryset = WorkLocation.objects.all()
    serializer_class = WorkLocationSerializer

# -------------------------- ABOUT US -------------------------- #

class CoreCompetencyViewSet(viewsets.ModelViewSet):
    queryset = CoreCompetency.objects.all()
    serializer_class = CoreCompetencySerializer

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

# -------------------------- OUR SERVICES -------------------------- #

class SubAreaViewSet(viewsets.ModelViewSet):
    queryset = SubArea.objects.all()
    serializer_class = SubAreaSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# -------------------------- PRACTICE AREAS -------------------------- #

class PracticeAreaViewSet(viewsets.ModelViewSet):
    queryset = PracticeArea.objects.all()
    serializer_class = PracticeAreaSerializer

class MilestoneWorkViewSet(viewsets.ModelViewSet):
    queryset = MilestoneWork.objects.all()
    serializer_class = MilestoneWorkSerializer

# -------------------------- OUR TEAM -------------------------- #

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

# -------------------------- OUR WORK & REACH -------------------------- #

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class WorkReachViewSet(viewsets.ModelViewSet):
    queryset = WorkReach.objects.all()
    serializer_class = WorkReachSerializer

# -------------------------- OUR PRODUCTS -------------------------- #

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# -------------------------- REQUEST FORM -------------------------- #

class RequestFormViewSet(viewsets.ModelViewSet):
    queryset = RequestForm.objects.all()
    serializer_class = RequestFormSerializer

# -------------------------- PHOTO GALLERY -------------------------- #

class PhotoGalleryViewSet(viewsets.ModelViewSet):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer

# -------------------------- CONTACT -------------------------- #

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
