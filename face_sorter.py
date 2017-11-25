#!/usr/bin/env python

import csv
import re
import os
import shutil

# Run through the structured .txt files
for file_nbr in range(0,4):
  filename='openu/fold_frontal_'+str(file_nbr)+'_data.txt'

  # Read files as .csv with tab delimiter
  with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    reader.next()  # Skip header
    exceptions = []
    for row in reader:
      user_id, original_image, face_id, age, gender, x, y, dx, dy, tilt_ang, fiducial_yaw_angle, fiducial_score = row
      # exclude files that are neither man or woman
      if  gender not in ['m', 'f']:
        exceptions.append(row)
      # sort all man/woman files to the right directory
      else:
        gender_name = {'m': 'male', 'f': 'female'}
        age = re.sub(r'[\(\)\s]', '', age)
        age = re.sub(',', '_', age)
        src = "openu/faces/"+user_id+"/coarse_tilt_aligned_face."+face_id+"."+original_image
        dir = "./openu/"+gender_name[gender]+"_"+age
        # if doesn't exist, create the corresponding directory
        if not os.path.isdir(dir):
           os.mkdir(dir)
        # copy the file to the corresponding directory
        shutil.copy(src, dir)
