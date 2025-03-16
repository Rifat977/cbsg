# urls.py

from django.urls import path
from .views import *

app_name = "core"

urlpatterns = [
    path("company-profile/", CompanyProfileViewSet.as_view({'get': 'list'}), name="company-profile"),
    path("company-profile/<int:pk>/", CompanyProfileViewSet.as_view({'get': 'retrieve'}), name="company-profile-detail"),

    path("home-banners/", HomeBannerViewSet.as_view({'get': 'list'}), name="home-banners"),
    path("home-banners/<int:pk>/", HomeBannerViewSet.as_view({'get': 'retrieve'}), name="home-banners-detail"),

    path("recent-projects/", RecentProjectViewSet.as_view({'get': 'list'}), name="recent-projects"),
    path("recent-projects/<int:pk>/", RecentProjectViewSet.as_view({'get': 'retrieve'}), name="recent-projects-detail"),

    path("testimonials/", TestimonialViewSet.as_view({'get': 'list'}), name="testimonials"),
    path("testimonials/<int:pk>/", TestimonialViewSet.as_view({'get': 'retrieve'}), name="testimonials-detail"),

    path("core-competencies/", CoreCompetencyViewSet.as_view({'get': 'list'}), name="core-competencies"),
    path("core-competencies/<int:pk>/", CoreCompetencyViewSet.as_view({'get': 'retrieve'}), name="core-competencies-detail"),

    path("about-us/", AboutViewSet.as_view({'get': 'list'}), name="about-us"),
    path("about-us/<int:pk>/", AboutViewSet.as_view({'get': 'retrieve'}), name="about-us-detail"),

    path("year-ranges/", YearRangeViewSet.as_view({'get': 'list'}), name="year-ranges"),
    path("year-ranges/<int:pk>/", YearRangeViewSet.as_view({'get': 'retrieve'}), name="year-ranges-detail"),

    path("history-timelines/", HistoryTimelineViewSet.as_view({'get': 'list'}), name="history-timelines"),
    path("history-timelines/<int:pk>/", HistoryTimelineViewSet.as_view({'get': 'retrieve'}), name="history-timelines-detail"),

    path("strategic-partners/", StrategicPartnerViewSet.as_view({'get': 'list'}), name="strategic-partners"),
    path("strategic-partners/<int:pk>/", StrategicPartnerViewSet.as_view({'get': 'retrieve'}), name="strategic-partners-detail"),

    path("sub-service-areas/", SubServiceAreaViewSet.as_view({'get': 'list'}), name="sub-service-areas"),
    path("sub-service-areas/<int:pk>/", SubServiceAreaViewSet.as_view({'get': 'retrieve'}), name="sub-service-areas-detail"),

    path("assignments/", AssignmentViewSet.as_view({'get': 'list'}), name="assignments"),
    path("assignments/<int:pk>/", AssignmentViewSet.as_view({'get': 'retrieve'}), name="assignments-detail"),

    path("service-intros/", ServiceIntroViewSet.as_view({'get': 'list'}), name="service-intros"),
    path("service-intros/<int:pk>/", ServiceIntroViewSet.as_view({'get': 'retrieve'}), name="service-intros-detail"),

    path("practice-areas/", PracticeAreaViewSet.as_view({'get': 'list'}), name="practice-areas"),
    path("practice-areas/<int:pk>/", PracticeAreaViewSet.as_view({'get': 'retrieve'}), name="practice-areas-detail"),

    path("team-members/", TeamMemberViewSet.as_view({'get': 'list'}), name="team-members"),
    path("team-members/<int:pk>/", TeamMemberViewSet.as_view({'get': 'retrieve'}), name="team-members-detail"),

    path("milestone-works/", MilestoneWorkViewSet.as_view({'get': 'list'}), name="milestone-works"),
    path("milestone-works/<int:pk>/", MilestoneWorkViewSet.as_view({'get': 'retrieve'}), name="milestone-works-detail"),

    path("work-locations/", WorkLocationViewSet.as_view({'get': 'list'}), name="work-locations"),
    path("work-locations/<int:pk>/", WorkLocationViewSet.as_view({'get': 'retrieve'}), name="work-locations-detail"),

    path("reports/", ReportViewSet.as_view({'get': 'list'}), name="reports"),
    path("reports/<int:pk>/", ReportViewSet.as_view({'get': 'retrieve'}), name="reports-detail"),

    path("blog-posts/", BlogPostViewSet.as_view({'get': 'list'}), name="blog-posts"),
    path("blog-posts/<int:pk>/", BlogPostViewSet.as_view({'get': 'retrieve'}), name="blog-posts-detail"),

    path("request-forms/", RequestFormViewSet.as_view({'get': 'list', 'post': 'create'}), name="request-forms"),
    path("request-forms/<int:pk>/", RequestFormViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name="request-forms-detail"),

]
