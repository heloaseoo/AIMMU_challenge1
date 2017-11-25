#!/usr/bin/env python

import os
import random
import shutil

# defines the proportion of data for validation and test
VAL_PROP = 0.2
TEST_PROP = 0.1
# define the folder paths
TRAIN_DIR = './data/train_dir/'
VAL_DIR = './data/val_dir/'
TEST_DIR = './data/test_dir/'

# creates a list that will hold all subfolders indexed by gender/age
folders = []
for name in os.listdir(TRAIN_DIR):
    folders.append(name)
# run through each subfolder and move random files to VAL_DIR and TEST_DIR according to their proportion
for i in range(1,len(folders)):
	length=len([nbr for nbr in os.listdir(TRAIN_DIR+folders[i])])
	val_counter=int(round(VAL_PROP*length))
	test_counter=int(round(TEST_PROP*length))

	for val in range(0,val_counter):
		src=TRAIN_DIR+folders[i]+'/'+random.choice(os.listdir(TRAIN_DIR+folders[i]))
		dst=VAL_DIR+folders[i]
		shutil.move(src,dst)

	for test in range(0,test_counter):
		src=TRAIN_DIR+folders[i]+'/'+random.choice(os.listdir(TRAIN_DIR+folders[i]))
		dst=TEST_DIR+folders[i]
		shutil.move(src,dst)

	"""
		Print the settings for each folder (useful to check/debug)

	print folders[i]
	print length
	print val_counter
	print test_counter
	"""