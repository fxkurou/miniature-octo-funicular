from django.urls import path

from api.sca.views import (
    SpyCatDetailView, SpyCatListCreateView,
    MissionDetailView, MissionListCreateView
)

urlpatterns = [
    path("spycats/", SpyCatListCreateView.as_view(), name="spycat_list_create"),
    path("spycats/<int:pk>/", SpyCatDetailView.as_view(), name="spycat_detail"),
    path("missions/", MissionListCreateView.as_view(), name="mission_list_create"),
    path("missions/<int:pk>/", MissionDetailView.as_view(), name="mission_detail"),
]
