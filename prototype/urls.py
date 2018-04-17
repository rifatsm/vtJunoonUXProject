from django.conf.urls import url

from . import views

app_name = "prototype"

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'about/$', views.about, name="about"),
    url(r'people/$', views.people, name="people"),
    url(r'contact/$', views.contact, name="contact"),
    url(r'gallery/$', views.gallery, name="gallery"),
    url(r'fund/$', views.fund, name="fund"),
    url(r'signup/$', views.signup, name="signup"),
    url(r'login/$', views.login, name="login"),
    url(r'in/$', views.in_land, name="in"),
    url(r'in_us/$', views.in_land_us, name="in_us"),
    url(r'practicevideos/$', views.prac, name="prac"),
    url(r'practicevideos_us/$', views.prac_user, name="prac_user"),




]