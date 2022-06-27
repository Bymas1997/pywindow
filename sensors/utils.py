#!/usr/bin/python
# -*- coding: utf-8 -*-

import time


class Scheduler(object):
    """ Inspection scheduler """

    def __init__(
        self,
        max_fps: int = 30,
        is_schedule_time: bool = True
    ) -> None:
        self.__max_fps = max_fps
        self.__is_schedule_time = is_schedule_time
        self.__min_interval = 1/self.__max_fps
        self.__prev_time = time.time()

    def set_max_fps(self, max_fps: int) -> None:
        """ Set the maximum fps value """
        self.__max_fps = max_fps
        self.__min_interval = 1 / max_fps

    def schedule_time(self):
        interval_offset = self.__min_interval - (time.time() - self.__prev_time)
        if interval_offset > 0.0:
            time.sleep(interval_offset)
            self.__prev_time = time.time()

    def __call__(self, **options) -> None:
        if self.__is_schedule_time:
            self.schedule_time()
