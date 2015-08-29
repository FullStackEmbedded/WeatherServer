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

from csv import writer
from io import StringIO

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from .models import Station

def index(request):
    """Show index page."""
    template = get_template("index.html")
    variables = Context({
        "head_title": "Open Weather Station",
        "page_title": "Open Weather Station",
        "page_body": "Open Weather Station is the reference project for Full "
                     "Stack Embedded 2016. We hope you like it!",
    })
    output = template.render(variables)
    return HttpResponse(output)

def csv_stations(request):
    """Return CSV of available stations."""
    response = StringIO()
    response.write("name,id,longitude,latitude,elevation,activated,deactivated,"
                   "description\r\n")
    csv_renderer = writer(response)
    csv_renderer.writerows(
        ((station.name, station.station_id, station.longitude,
          station.latitude, station.elevation, station.activated,
          station.deactivated, station.description))
        for station in Station.objects.all())
    response.seek(0)
    return HttpResponse(response)

