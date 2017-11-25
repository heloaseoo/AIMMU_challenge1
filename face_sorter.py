#!/usr/bin/env python

import csv
import re
import os
import shutil

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
      src = "openu/faces/"+user_id+"/coarse_tilt_aligned_face."+face_id+"."+original_image
      dir = "./openu/"+gender_name[gender]+"_"+age
      if not os.path.isdir(dir):
         os.mkdir(dir)
      shutil.copy(src, dir)
