#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
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


# sensor_config = {
#     "receiver": show_result,          # Display function name
#     "data_path": r"./profile_1.txt",  # Data file
#     "mode": "trigger",                # Display mode
#     "fps": 20                         # Maximum fps
# }

sensor = FakeSensor(
    receiver=show_result,
    data_path=r"./profile_1.txt",
    mode="live",
    fps=20
)

# while True:
#     inp = input("Input: ")
#     if inp.lower() == "q":
#         break
#     else:
#         sensor.trigger()
#     print("Loop end in one cycle.")

to_wait: bool = False
is_waiting: bool = False
is_notified: bool = False
start_time = time.time()
sensor.notify()
while True:
    if time.time() - start_time <= 5.0:
        time.sleep(0.05)
    elif not to_wait and not is_waiting:
        to_wait = True
    elif is_waiting and 7.0 <= time.time() - start_time <= 10.0 and not is_notified:
        print("Trying to notify...")
        sensor.notify()
        is_notified = True
    elif 12.0 < time.time() - start_time:
        break

    if to_wait:
        print("Trying to block the thread:")
        to_wait = False
        is_waiting = True
        sensor.wait()
sensor.exit()
