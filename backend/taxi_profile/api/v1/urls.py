from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    DocumentViewSet,
    DriverProfileViewSet,
    InviteCodeViewSet,
    NotificationViewSet,
    UserProfileViewSet,
)

router = DefaultRouter()
router.register("invitecode", InviteCodeViewSet)
router.register("document", DocumentViewSet)
router.register("notification", NotificationViewSet)
router.register("userprofile", UserProfileViewSet)
router.register("driverprofile", DriverProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
