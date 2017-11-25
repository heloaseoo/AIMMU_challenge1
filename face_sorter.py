#!/usr/bin/env python

import csv
import re

FILENAME = 'openu/fold_frontal_0_data.txt'

with open(FILENAME, 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter='\t')
  reader.next()  # Skip header
  exceptions = []
  for row in reader:
    user_id, original_image, face_id, age, gender, x, y, dx, dy, tilt_ang, fiducial_yaw_angle, fiducial_score = row
    if  gender not in ['m', 'f']:
      exceptions.append(row)
    else:
      gender_name = {'m': 'male', 'f': 'female'}
      age = re.sub(r'[\(\)\s]', '', age)
      age = re.sub(',', '_', age)
      print 'mkdir openu/%s_%s/' % (gender_name[gender], age)
      print 'cp openu/faces/%s/coarse_tilt_aligned_face.%s.%s openu/%s_%s/' % (user_id, face_id, original_image, gender_name[gender], age)