#!/usr/bin/python
# -*- coding: utf-8 -*-

import typing as t
from abc import abstractmethod
from collections import OrderedDict
from threading import Thread
from threading import Condition as ThreadCondition
from queue import Queue as ThreadQueue
from multiprocessing import Process
from multiprocessing import Condition as ProcessCondition
from multiprocessing import Queue as ProcessQueue
from .utils import Scheduler


class AbstractThreadSensor(Thread):
    """ Abstract thread sensor object, which serves as a child class of a Thread. """

    def __init__(
        self,
        receiver: t.Optional[t.Callable] = None,
        mode: str = "live",
        fps: int = 30,
        data_queue: t.Optional[ThreadQueue] = None,
        result_queue: t.Optional[ThreadQueue] = None,
        add_condition: bool = True,
        connect_while_init: bool = True,
        name: t.Optional[str] = None,
        **options
    ) -> None:
        super(AbstractThreadSensor, self).__init__()
        self._receiver: t.Optional[t.Callable] = receiver
        self._mode = mode  # Sensor's mode, "live" or "trigger".
        self._fps = fps  # Maximal refreshing frequency while in live mode.
        self._data_queue = data_queue
        self._result_queue = result_queue
        self._name = name or "thread_sensor"
        self._scheduler = Scheduler(max_fps=fps)
        self._options = options

        if add_condition:
            self._condition = ThreadCondition()
            # self._condition.acquire()
        else:
            self._condition = None
        if connect_while_init:
            self.connect()

    @property
    def name(self) -> str:
        """ Returns the worker's name. """
        return self._name

    @property
    def data_queue(self) -> ThreadQueue:
        """ Returns the thread's data queue. """
        return self._data_queue

    @property
    def result_queue(self) -> ThreadQueue:
        """ Returns the thread's result queue. """
        return self._result_queue

    @abstractmethod
    def connect(self, **options) -> bool:
        """ Connecting ot the sensor device, returns whether the device has been connected. """
        pass

    @abstractmethod
    def disconnect(self, **options) -> bool:
        """ Disconnecting ot the sensor device, returns whether the device has been disconnected. """
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        """ Returns whether the sensor device has been correctly connected. """
        pass

    @abstractmethod
    def trigger(self, **options) -> bool:
        """ Trigger the sensor while in trigger mode, it returns whether the sensor has been triggered. """
        pass

    @abstractmethod
    def wait(self, timeout: t.Optional[float] = None, **options) -> None:
        """ Block the thread. """
        pass

    @abstractmethod
    def notify(self, **options) -> None:
        """ Wake up the thread. """
        pass

    @abstractmethod
    def exit(self, **options) -> None:
        """ Function for safely exit the thread running loop. """
        pass


class AbstractProcessSensor(Process):
    """ Abstract process sensor object, which serves as a child class of a Process. """

    def __init__(
        self,
        receiver: t.Optional[t.Callable] = None,
        mode: str = "live",
        fps: int = 30,
        data_queue: t.Optional[ProcessQueue] = None,
        result_queue: t.Optional[ProcessQueue] = None,
        add_condition: bool = True,
        connect_while_init: bool = True,
        name: t.Optional[str] = None,
        **options
    ) -> None:
        super(AbstractProcessSensor, self).__init__()
        self._receiver: t.Optional[t.Callable] = receiver
        self._mode = mode  # Sensor's mode, "live" or "trigger".
        self._fps = fps    # Maximal refreshing frequency while in live mode.
        self._data_queue = data_queue
        self._result_queue = result_queue
        self._name = name or "process_sensor"
        self._config_cache: t.Dict[str, t.Dict[str, t.Any]] = OrderedDict()
        self._scheduler = Scheduler(max_fps=fps)
        self._options = options

        if data_queue is None:
            self._data_queue = ProcessQueue(maxsize=16)
        if result_queue is None:
            self._result_queue = ProcessQueue(maxsize=1)
        if add_condition:
            self._condition = ProcessCondition()
            self._condition.acquire()
        else:
            self._condition = None
        if connect_while_init:
            self.connect()

    @property
    def name(self) -> str:
        """ Returns the worker's name. """
        return self._name

    @property
    def data_queue(self) -> ThreadQueue:
        """ Returns the process data queue. """
        return self._data_queue

    @property
    def result_queue(self) -> ThreadQueue:
        """ Returns the process result queue. """
        return self._result_queue

    @abstractmethod
    def connect(self, **options) -> bool:
        """ Connecting ot the sensor device, returns whether the device has been connected. """
        pass

    @abstractmethod
    def disconnect(self, **options) -> bool:
        """ Disconnecting ot the sensor device, returns whether the device has been disconnected. """
        pass

    @abstractmethod
    def is_connected(self) -> bool:
        """ Returns whether the sensor device has been correctly connected. """
        pass

    @abstractmethod
    def trigger(self, **options) -> bool:
        """ Trigger the sensor while in trigger mode, it returns whether the sensor has been triggered. """
        pass

    @abstractmethod
    def wait(self, timeout: t.Optional[float] = None, **options) -> None:
        """ Block the process. """
        pass

    @abstractmethod
    def notify(self, **options) -> None:
        """ Wake up the process. """
        pass

    @abstractmethod
    def exit(self, **options) -> None:
        """ Function for safely exit the process running loop. """
        pass

    def _cache_config(self, configuration: t.Union[t.Dict[str, t.Any], t.List[t.Dict[str, t.Any]]]) -> None:
        """ Cache configs into the config cache, this function is to be called inside the process running loop. """
        if isinstance(configuration, dict):
            self._cache_single_config(configuration)
        elif isinstance(configuration, list):
            for cfg in configuration:
                self._cache_single_config(cfg)

    def _cache_single_config(self, configuration: t.Dict[str, t.Any]):
        """ Cache a single piece of configuration, the configuration dictionary should have the following format:
            configuration = {
                "module": str
                "key": str,
                "value": any,
                "index": int,
                "name": str
            }
        """
        key, value, module = configuration.get("key"), configuration.get("value"), configuration.get("module")
        if module is None:
            config_key = key
        else:
            config_key = module + '-' + key
        self._config_cache[config_key] = configuration

