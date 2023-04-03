from rest_framework import routers
from accounts.views import AccountViewSet
from posts.views import PostViewSet
from events.views import EventViewSet
from support.views import SupportViewset
from careers.views import CareerViewset
from volunteers.views import VolunteerViewset
from contacts.views import ContactViewset
from donations.views import DonationViewset

router = routers.DefaultRouter()

router.register(r'accounts', AccountViewSet)
router.register(r'posts',PostViewSet)
router.register(r'events',EventViewSet)
router.register(r'careers',CareerViewset)
router.register(r'volunteers',VolunteerViewset)
router.register(r'contact',ContactViewset)
router.register(r'donations',DonationViewset)