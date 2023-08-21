from django.urls import path, include
from rest_framework import routers

from theatre.views import (
    GenreViewSet,
    ActorViewSet,
    TheatreHallViewSet,
    PlayViewSet,
    PerformanceViewSet,
    ReservationViewSet,
)

router = routers.DefaultRouter()
router.register("plays", PlayViewSet)
router.register("performances", PerformanceViewSet)
router.register("reservations", ReservationViewSet)
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("theatres", TheatreHallViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "theatre"
