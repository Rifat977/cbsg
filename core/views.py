from rest_framework import viewsets
from .models import *
from .serializers import *
class CompanyProfileViewSet(viewsets.ModelViewSet):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer

class HomeBannerViewSet(viewsets.ModelViewSet):
    queryset = HomeBanner.objects.all()
    serializer_class = HomeBannerSerializer

class RecentProjectViewSet(viewsets.ModelViewSet):
    queryset = RecentProject.objects.all()
    serializer_class = RecentProjectSerializer

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class CoreCompetencyViewSet(viewsets.ModelViewSet):
    queryset = CoreCompetency.objects.all()
    serializer_class = CoreCompetencySerializer

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class YearRangeViewSet(viewsets.ModelViewSet):
    queryset = YearRange.objects.all()
    serializer_class = YearRangeSerializer

class HistoryTimelineViewSet(viewsets.ModelViewSet):
    queryset = HistoryTimeline.objects.all()
    serializer_class = HistoryTimelineSerializer

class StrategicPartnerViewSet(viewsets.ModelViewSet):
    queryset = StrategicPartner.objects.all()
    serializer_class = StrategicPartnerSerializer

class SubServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = SubServiceArea.objects.all()
    serializer_class = SubServiceAreaSerializer

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class ServiceIntroViewSet(viewsets.ModelViewSet):
    queryset = ServiceIntro.objects.all()
    serializer_class = ServiceIntroSerializer

class PracticeAreaViewSet(viewsets.ModelViewSet):
    queryset = PracticeArea.objects.all()
    serializer_class = PracticeAreaSerializer

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all().order_by('priority')
    serializer_class = TeamMemberSerializer

class MilestoneWorkViewSet(viewsets.ModelViewSet):
    queryset = MilestoneWork.objects.all()
    serializer_class = MilestoneWorkSerializer

class WorkLocationViewSet(viewsets.ModelViewSet):
    queryset = WorkLocation.objects.all()
    serializer_class = WorkLocationSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class RequestFormViewSet(viewsets.ModelViewSet):
    queryset = RequestForm.objects.all()
    serializer_class = RequestFormSerializer

class PhotoGalleryViewSet(viewsets.ModelViewSet):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer