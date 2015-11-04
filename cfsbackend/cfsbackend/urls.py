"""
    cfsbackend URL Configuration
"""
from django.conf.urls import include, url
from rest_framework import routers

from core import views

router = routers.DefaultRouter()

router.register(r'calls_sources', views.CallSourceViewSet)
router.register(r'calls_units', views.CallUnitViewSet)
router.register(r'nature', views.NatureViewSet)
router.register(r'close_codes', views.CloseCodeViewSet)
router.register(r'cities', views.CityViewSet)
router.register(r'sectors', views.SectorViewSet)
router.register(r'districts', views.DistrictViewSet)
router.register(r'beats', views.BeatViewSet)

router.register(r'calls', views.CallViewSet)

# You must use the optional 3rd parameter here. or otherwise it changes the URL for calls.
# the same holds true for any double-usage of the same queryset model in the ViewSet.
router.register(r'calls_overview', views.CallOverviewViewSet, 'callsoverview')

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^api/officer_allocation/', views.OfficerAllocationView.as_view()),
    url(r'^api/overview/', views.OverviewView.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^$', views.DashboardView.as_view()),
    url(r'^calls', views.CallListView.as_view()),
    url(r'^predictive', views.PredictiveView.as_view()),
]
