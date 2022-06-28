#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import copy
import random
import typing as t
from queue import Queue as ThreadQueue
from .abstract import AbstractThreadSensor


class FakeSensor(AbstractThreadSensor):
    """ Fake sensor object. """

    def __init__(
        self,
        receiver: t.Optional[t.Callable] = None,
        mode: str = "trigger",
        fps: int = 30,
        data_queue: t.Optional[ThreadQueue] = None,
        result_queue: t.Optional[ThreadQueue] = None,
        add_condition: bool = True,
        connect_while_init: bool = True,
        name: t.Optional[str] = None,
        **options
    ) -> None:
        if data_queue is None:
            data_queue = ThreadQueue(maxsize=16)
        if result_queue is None:
            result_queue = ThreadQueue(maxsize=1)
        self._is_connected: bool = False
        self._is_waiting: bool = True
        super(FakeSensor, self).__init__(receiver, mode, fps, data_queue, result_queue, add_condition,
                                         connect_while_init, name, **options)
        self._data = self._load_data(options.get("data_path"))
        self._is_triggered: bool = False or self._mode == "live"
        self._is_exit: bool = False
        self.start()

    @staticmethod
    def _load_data(data_path: t.Optional[str]) -> t.List[t.List[float]]:
        """ Load the input data into a python list. If the file not exists, returns the fake data list. """
        data_list: t.List[t.List[float]] = list()
        if data_path is None or not os.path.isfile(data_path):
            intervals: int = 1000
            for i in range(intervals):
                data_list.append([-8.0 + i * 16.0 / intervals, 0.0])
        else:
            with open(data_path, 'r') as f:  # 以只读形式打开某.txt文件
                for line in f:
                    line = line.strip('\n')  # 去掉换行符
                    line = line.split('\t')  # 分割掉两列数据之间的制表符
                    data_list.append([float(line[0]), float(line[1])])
                f.close()
        return data_list

    def connect(self, **options) -> bool:
        """ Connecting ot the sensor device, returns whether the device has been connected. """
        self._is_connected = True
        return self._is_connected

    def disconnect(self, **options) -> bool:
        """ Disconnecting ot the sensor device, returns whether the device has been disconnected. """
        self._is_connected = False
        return self._is_connected

    def is_connected(self) -> bool:
        """ Returns whether the sensor device has been correctly connected. """
        return self._is_connected

    def trigger(self, **options) -> bool:
        """ Trigger the sensor while in trigger mode, it returns whether the sensor has been triggered. """
        if not self._is_connected or self._mode != "trigger" or self._is_triggered:
            return False
        self._data_queue.put({"trigger": True})
        return True

    def wait(self, timeout: t.Optional[float] = None, **options) -> None:
        """ Block the thread. """
        self._is_waiting = True

    def notify(self, **options) -> None:
        """ Wake up the thread. """
        self._data_queue.put({"notify": True})

    def exit(self, **options) -> None:
        """ Function for safely exit the thread running loop. """
        self.disconnect()
        if self._data_queue.full():
            self._data_queue.get()
        self._data_queue.put({"exit": True})
        while self.is_alive() and self.result_queue.full():
            self._result_queue.get()

    def run(self) -> None:
        """ Definition for running the sensor thread looping. """
        num_data = len(self._data)
        crop_range = int(0.15 * num_data)

        while True:
            if self._pre_looping_condition():
                data = self._data_queue.get()
                if "trigger" in data and not self._is_waiting:
                    self._is_triggered = True
                elif "notify" in data and self._is_waiting:
                    self._is_waiting = False
                elif "config" in data:
                    pass
                elif "exit" in data:
                    break

            if not self._is_triggered or self._is_waiting:
                self._scheduler()
                continue
            front_index: int = random.randint(0, crop_range)
            end_index: int = random.randint(num_data-crop_range, num_data)
            data = copy.deepcopy(self._data[front_index:end_index])
            if self._receiver is not None:
                self._receiver(data)
            else:
                self._result_queue.put({"data": data})

            self._is_triggered = self._mode == "live"
            self._scheduler()

    def _pre_looping_condition(self) -> bool:
        """ Condition before each loop. """
        if self._mode == "trigger" or self._is_waiting:
            return True
        elif self._mode == "live":
            return not self._data_queue.empty()
        else:
            raise ValueError("Unsupported camera worker mode.")