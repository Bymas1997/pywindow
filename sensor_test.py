#!/usr/bin/python
# -*- coding: utf-8 -*-

import typing as t
from sensors import FakeSensor


def show_result(data_list: t.List[t.List[float]]) -> None:
    """ Displaying the result list. The input data list has the following format:
        data_list: [
            [x0, y0],
            [x1, y1],
            ...
        ]
    """
    print("The number of data is", len(data_list), ".")


sensor_config = {
    "receiver": show_result,          # Display function name
    "data_path": r"./profile_1.txt",  # Data file
    "mode": "trigger",                # Display mode
    "fps": 20                         # Maximum fps
}


sensor = FakeSensor(**sensor_config)
while True:
    inp = input("Input: ")
    if inp.lower() == "q":
        break
    else:
        sensor.trigger()
    print("Loop end in one cycle.")
sensor.exit()
