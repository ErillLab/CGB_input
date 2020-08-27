#!/usr/bin/env python
import time

from cgb_input import create_file

seconds_per_minute = 60

input_file = 'pseudomon_family.json'

start_time = time.time()

cgb_input_file = create_file(input_file)

overall_time_minutes = (int(time.time() - start_time)) / seconds_per_minute

print '\nTime to create input file:', overall_time_minutes, 'minutes'
