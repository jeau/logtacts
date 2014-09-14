from django.conf.urls import patterns, include, url
from django.contrib import admin

from contacts.views import (
    contact_views,
    log_views,
)

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'logtacts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^$',
        contact_views.ContactListView.as_view(),
        name='contacts-list',
    ),
    url(
        r'^(?P<pk>\d+)/$',
        contact_views.ContactView.as_view(),
        name='contacts-view',
    ),
    url(
        r'^new$',
        contact_views.CreateContactView.as_view(),
        name='contacts-new',
    ),
    url(
        r'^edit/(?P<pk>\d+)/$',
        contact_views.EditContactView.as_view(),
        name='contacts-edit',
    ),
    url(
        r'^delete/(?P<pk>\d+)/$',
        contact_views.DeleteContactView.as_view(),
        name='contacts-delete',
    ),
    url(
        r'^log/edit/(?P<pk>\d+)/$',
        log_views.EditLogView.as_view(),
        name='log-edit',
    ),
    url(
        r'^log/delete/(?P<pk>\d+)/$',
        log_views.DeleteLogView.as_view(),
        name='log-delete',
    ),
    url(
        r'^tags/new$',
        contact_views.CreateTagView.as_view(),
        name='tags-new',
    ),
    url(
        r'^tagged/(?P<pk>\d+)/$',
        contact_views.TaggedContactListView.as_view(),
        name='contacts-tagged',
    ),
)