# .. Imports
from rest_framework_nested import routers
from django.conf.urls import patterns, url, include 

from thinkster_django_angular_boilerplate.views import IndexView

from authentication.views import AccountViewSet, LoginView, LogoutView

<<<<<<< HEAD
from posts.views import AccountPostsViewSet, PostViewSet
=======

>>>>>>> 9984e5de576085e357181c1f3ba0783fa40b1d91

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

<<<<<<< HEAD
router.register(r'posts', PostViewSet)

accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account'
)
accounts_router.register(r'posts', AccountPostsViewSet)

=======
>>>>>>> 9984e5de576085e357181c1f3ba0783fa40b1d91
urlpatterns = patterns(
     '', 

    url(r'^api/v1/', include(router.urls)),

    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),

    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),

<<<<<<< HEAD
    url(r'^api/v1/', include(router.urls)),
  
  	url(r'^api/v1/', include(accounts_router.urls)),

    url('^.*$', IndexView.as_view(), name='index'),


=======
    url('^.*$', IndexView.as_view(), name='index'),
>>>>>>> 9984e5de576085e357181c1f3ba0783fa40b1d91
)