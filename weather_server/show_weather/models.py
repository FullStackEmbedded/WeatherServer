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

from django.db import models


class Station(models.Model):
    """Metadata for the observing station."""
    #: Unique station identifier
    station_id = models.IntegerField()
    #: Station's longitude in WGS84
    station_longitude = models.DecimalField(max_digits=7, decimal_places=4)
    #: Station's latitude in WGS84
    station_latitude = models.DecimalField(max_digits=6, decimal_places=4)
    #: Station's elevation over mean sea level in WGS84
    station_elevation = models.FloatField()
    #: Station's informal name
    station_name = models.CharField(max_length=80)
    #: Date of station activation.
    station_activated = models.DateTimeField('Station activated')
    #: Station's deactivation date. A reactivated station is a new station.
    station_deactivated = models.DateTimeField('Station deactivated')
    station_description = models.CharField(max_length=200)


class Observation(models.Model):
    """
    Weather observation.

    Observations are always in SI units.
    """
    obs_date = models.DateTimeField('observation date')
    #: Observing station
    obs_station = models.ForeignKey(Station)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    #: In %
    relative_humidity = models.DecimalField(max_digits=3, decimal_places=1)
    #: In mm
    precipitation = models.IntegerField()
    #: In m/s
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    #: In degrees clockwise from cartographic north
    wind_direction = models.IntegerField()
    #: In hPa
    pressure = models.IntegerField()
