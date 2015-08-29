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

from django.contrib import admin

from .models import Station, Observation

class StationAdmin(admin.ModelAdmin):
    list_display = ("name", "longitude", "latitude", "elevation", "description")

class ObservationAdmin(admin.ModelAdmin):
    list_display = ("obs_date",
                    "station",
                    "temperature",
                    "relative_humidity",
                    "precipitation",
                    "wind_speed",
                    "wind_direction",
                    "pressure")
    list_filter = ["obs_date"]

for model, administrator in ((Station, StationAdmin),
                             (Observation, ObservationAdmin)):
    admin.site.register(model, administrator)
