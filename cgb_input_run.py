#!/usr/bin/env python

import time

from cgb_input import create_file

seconds_per_minute = 60

input_file = 'pseudomon_family.json'

start_time = time.time()

cgb_input_file = create_file(input_file)

end_time = time.time()

tot_time = end_time - start_time

rem_seconds = tot_time % seconds_per_minute

tot_time_min = int(tot_time - rem_seconds) // seconds_per_minute

print'\nTime to create input file:', tot_time_min, 'min.', round(rem_seconds), 'sec.'