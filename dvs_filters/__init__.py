'''
A Python class to simulate a Dynamic Vision Sensor through first-differencing
of current and previous image from an ordinary camera.

Copyright (C) 2023 Simon D. Levy, Armando Mendez-Anastasio

This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation; either version 2 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program; if not, write to the Free Software Foundation, Inc., 51
Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
'''

import numpy as np

class NoiseFilter:

    def filter(self, events):

        filtered = np.zeros(events.shape)

        nz = np.where(events)

        for x,y in zip(nz[0], nz[1]):

            filtered[x,y] = events[x,y]

        return filtered
