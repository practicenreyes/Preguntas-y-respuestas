from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'segundo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^preguntas/$', 'preguntasyrespuestas.views.index', name="preguntas"),
    url(r'^$', 'segundo.views.homepage', name="homepage"),
    url(r'^login/$', 'segundo.views.login_page', name="login"),
    url(r'^logout/$', 'segundo.views.logout_view', name="logout"),
    url(r'^preguntas/crear/$', 'preguntasyrespuestas.views.pregunta_crear', name="pregunta_crear"),
    url(r'^preguntas/editar/(?P<pregunta_id>\d+)/$', 'preguntasyrespuestas.views.pregunta_editar', name='pregunta_editar'),
    url(r'^preguntas/(?P<pregunta_id>\d+)/$', 'preguntasyrespuestas.views.pregunta_detalle', name='pregunta_detalle'),


    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
