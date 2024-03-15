# -*- coding: utf-8 -*-
#
# ,---------,       ____  _ __
# |  ,-^-,  |      / __ )(_) /_______________ _____  ___
# | (  O  ) |     / __  / / __/ ___/ ___/ __ `/_  / / _ \
# | / ,--'  |    / /_/ / / /_/ /__/ /  / /_/ / / /_/  __/
#    +------`   /_____/_/\__/\___/_/   \__,_/ /___/\___/
#
# Copyright (C) 2019 - 2020 Bitcraze AB
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, in version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import logging

from .memory_element import MemoryElement
from cflib.utils.callbacks import Syncer

logger = logging.getLogger(__name__)


class PAA3905Memory(MemoryElement):
    """Memory interface for reading the multiranger values"""

    def __init__(self, id, type, size, mem_handler):
        super(PAA3905Memory, self).__init__(id=id, type=type, size=size,
                                            mem_handler=mem_handler)
        self._read_finished_cb = None

    def new_data(self, mem, addr, data):
        """Callback for when new memory data has been fetched"""
        if mem.id == self.id and self._read_finished_cb:
            print(len(data))
            image_matrix = []
            for i in range(35):
                image_matrix.append(data[i*35:i*35+35])

            self._read_finished_cb(addr, image_matrix)

    def read_data(self, read_finished_cb):
        """Read image data from PAA3905"""
        self._read_finished_cb = read_finished_cb
        self.mem_handler.read(self, 0, 1225)

    def read_data_sync(self):
        """Write the saved LED-ring data to the Crazyflie"""
        syncer = Syncer()
        self.read_data(syncer.success_cb)
        syncer.wait()
        if syncer.is_success:
            return syncer.success_args[1]
        else:
            return None

    def read_failed(self, mem, addr):
        if mem.id == self.id:
            logger.debug('Read failed')

    def disconnect(self):
        self._read_finished_cb = None
