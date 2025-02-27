# urls.py

from django.urls import path
from .views import *

app_name = "core"

urlpatterns = [
    path('home-banner/', HomeBannerViewSet.as_view({'get': 'list'}), name='home-banner-list'),
    path('home-banner/<int:pk>/', HomeBannerViewSet.as_view({'get': 'retrieve'}), name='home-banner-detail'),

    path('recent-project/', RecentProjectViewSet.as_view({'get': 'list'}), name='recent-project-list'),
    path('recent-project/<int:pk>/', RecentProjectViewSet.as_view({'get': 'retrieve'}), name='recent-project-detail'),

    path('testimonial/', TestimonialViewSet.as_view({'get': 'list'}), name='testimonial-list'),
    path('testimonial/<int:pk>/', TestimonialViewSet.as_view({'get': 'retrieve'}), name='testimonial-detail'),

    path('work-location/', WorkLocationViewSet.as_view({'get': 'list'}), name='work-location-list'),
    path('work-location/<int:pk>/', WorkLocationViewSet.as_view({'get': 'retrieve'}), name='work-location-detail'),

    path('core-competency/', CoreCompetencyViewSet.as_view({'get': 'list'}), name='core-competency-list'),
    path('core-competency/<int:pk>/', CoreCompetencyViewSet.as_view({'get': 'retrieve'}), name='core-competency-detail'),

    path('about/', AboutViewSet.as_view({'get': 'list'}), name='about-list'),
    path('about/<int:pk>/', AboutViewSet.as_view({'get': 'retrieve',}), name='about-detail'),

    path('sub-area/', SubAreaViewSet.as_view({'get': 'list'}), name='sub-area-list'),
    path('sub-area/<int:pk>/', SubAreaViewSet.as_view({'get': 'retrieve'}), name='sub-area-detail'),

    path('service/', ServiceViewSet.as_view({'get': 'list'}), name='service-list'),
    path('service/<int:pk>/', ServiceViewSet.as_view({'get': 'retrieve'}), name='service-detail'),

    path('practice-area/', PracticeAreaViewSet.as_view({'get': 'list'}), name='practice-area-list'),
    path('practice-area/<int:pk>/', PracticeAreaViewSet.as_view({'get': 'retrieve'}), name='practice-area-detail'),

    path('milestone-work/', MilestoneWorkViewSet.as_view({'get': 'list'}), name='milestone-work-list'),
    path('milestone-work/<int:pk>/', MilestoneWorkViewSet.as_view({'get': 'retrieve'}), name='milestone-work-detail'),

    path('team-member/', TeamMemberViewSet.as_view({'get': 'list'}), name='team-member-list'),
    path('team-member/<int:pk>/', TeamMemberViewSet.as_view({'get': 'retrieve'}), name='team-member-detail'),

    path('assignment/', AssignmentViewSet.as_view({'get': 'list'}), name='assignment-list'),
    path('assignment/<int:pk>/', AssignmentViewSet.as_view({'get': 'retrieve'}), name='assignment-detail'),

    path('work-reach/', WorkReachViewSet.as_view({'get': 'list'}), name='work-reach-list'),
    path('work-reach/<int:pk>/', WorkReachViewSet.as_view({'get': 'retrieve'}), name='work-reach-detail'),

    path('product/', ProductViewSet.as_view({'get': 'list'}), name='product-list'),
    path('product/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'}), name='product-detail'),

    path('request-form/', RequestFormViewSet.as_view({'get': 'list'}), name='request-form-list'),
    path('request-form/<int:pk>/', RequestFormViewSet.as_view({'get': 'retrieve'}), name='request-form-detail'),

    path('photo-gallery/', PhotoGalleryViewSet.as_view({'get': 'list'}), name='photo-gallery-list'),
    path('photo-gallery/<int:pk>/', PhotoGalleryViewSet.as_view({'get': 'retrieve'}), name='photo-gallery-detail'),

    path('contact/', ContactViewSet.as_view({'get': 'list'}), name='contact-list'),
    path('contact/<int:pk>/', ContactViewSet.as_view({'get': 'retrieve'}), name='contact-detail'),
]
