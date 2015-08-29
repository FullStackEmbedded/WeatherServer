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

# Needed variables: Windspeed, precipitation, wind direction, temperature,
# humidity, air pressure

import pandas as pd

from show_weather.models import Observation, Station

obs = pd.read_csv("show_weather/utils/data_series.csv")
observing_station = Station(latitude=51.501364, longitude=-0.14189,
                            elevation=62, name="Daniel's apartment",
                            activated="2015-08-29",
                            description="Where the party's going down!",
                            station_id=0)
observing_station.save()

for idx, row in obs.iterrows():
    obs_date = row.iloc[0]
    station = observing_station
    temperature = row.t2m
    relative_humidity = row.relative_humidity
    precipitation = row.precipitation
    wind_speed = row.wind_speed
    wind_direction = row.wind_direction
    pressure = row.pressure
    Observation(obs_date=obs_date,
                station=observing_station,
                temperature=temperature,
                relative_humidity=relative_humidity,
                precipitation=precipitation,
                wind_speed=wind_speed,
                wind_direction=wind_direction,
                pressure=pressure).save()
