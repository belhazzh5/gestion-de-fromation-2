from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    FormationListView,
    FormationDetailView,
    join_formation,
    leave_formation,
    signUpView,
    profile,
    FormationCreateView,
    FormationUpdate,
    FormationDelete,
    formation_detail,
)

urlpatterns = [
    path("",FormationListView.as_view(),name="home"),
    path("profile/",profile,name="profile"),
    path("formation/create/",FormationCreateView.as_view(),name="create_formation"),
    path('user/register/', signUpView, name='register'),
    path("<slug:slug>/",FormationDetailView.as_view(),name="formation"),
    path("formation/<slug:slug>/",formation_detail,name="formation2"),
    path('formation/<slug:slug>/update',FormationUpdate.as_view(), name='update_formation'),
    path('formation/<slug:slug>/delete',FormationDelete.as_view(), name='delete_formation'),
    path('leave/<slug:slug>/',leave_formation, name='leave_formation'),
    path('join/<slug:slug>/',join_formation, name='join_formation'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
