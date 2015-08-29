# -*- coding: utf-8 -*-
"""
WeatherServer
Copyright (C) 2015  Full Stack Embedded

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""
from django.conf.urls import include, url
from django.contrib import admin
from show_weather.views import index, csv_observation_request, csv_stations

data_patterns = [
    url(r'^csv/'
        r'([0-9]+)/'                                         # Station ID
        r'([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2})'    # Start date
        r' - '
        r'([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2})$',  # End date
        csv_observation_request),
    url(r'^csv/stations/$', csv_stations)
]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^data/', include(data_patterns))
]
