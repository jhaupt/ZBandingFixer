#Z Periodicity Removal Script by Justine Haupt
#Created 9/30/17
#v1.0: 10/3/17

##This script will imprint a periodic structure onto the motion of the Z axis to compensate for incosistent (periodic) Z motion.
##This script does NOT do anything for Z wobble, only Z banding caused by z-axis movement error.
##For clarity, wobble is a periodic shift in layers due to lateral movement of the stage wheras banding referred to here
##is a periodic dilation in layers.

##Use with extreme care. This code has only been tested with Simplify3D output.

import numpy as np
import time
import fileinput
import glob
import os



##Modify these values as needed:
A = .055			# Amplitude of deviation. Find by trial and error.
center = .015		# Center of amplitude. E.g. with an amplitude of .025 and a center of .010, the extremes will be -.015 and +.035. Leave as 0.0 if unsure.
phase = 0.0			# Height above bed where deviation is 0 with positive derivative. May be difficult to measure. Trial and error likely needed to find it.

##Constants intrinsic to the printer design. Modify to suit your machine:
pitch = 3.0			# Leadscrew pitch in mm. This defines the period of the deviation.
stepsz = .005		# 1 step of the Z motors moves the bed this distance in mm. Needed to avoid lost steps due to microstep rounding errors.





## This function defines the shape of the deviation.
def modz(zval):
	mz = -1 * (A * np.sin( (2*(1/pitch))* np.pi * (zval - phase) ) + center)		#Modification function.
	mz = round(stepsz * round(mz/stepsz),3)								#Round mz value to the Z step resolution.
	mz = zval + mz														#Add output of function to z value.
	return mz

list_of_files = glob.glob('./*.gcode') 				# Get list of all gcode files in current directory.
latest_file = max(list_of_files, key=os.path.getctime)		#From that list, find the most recent one.

print '\nLoading ' + latest_file + '\n'

with open(latest_file, 'a') as temp:				#Append comment to gcode file indicating that it's been modified by this script.
	temp.write('; ####This gcode has been post-processed by ZBandingFixer.py####\n')

for line in fileinput.input(latest_file, inplace=True): #%(filename))			#Opens the gcode file using a module where any time we print something, it overrites whatever was in that line of the file.
	if ';' in line:			#If there's a ';' just rewrite the old line
		print line,
	elif 'X' in line:		#If there's an 'X' just rewrite the old line
		print line,
	elif 'Y' in line:		#If there's a 'Y' just rewrite the old line
		print line,
	elif 'E' in line:		#If there's an 'E' just rewrite the old line
		print line,
	elif 'Z' in line:							#If a line has a Z (but none of the above characters), then it's a line we want to change. We...
		s = line							#...call it 's' (for string)...
		num_char = (".", "+", "-")			#...define a list of characters to also look for (comes up in a little bit)...

		tokens = s.split()					#...split each word in 's' into a separate token...
		for token in tokens:				#...for each of those words...

		    if token.startswith("Z"):			#...if it starts with the character 'Z'...
		        num = ""
		        for char in token:
		            # print(char)
		            if char.isdigit() or (char in num_char):	#...and	also includes either a digit or one of the characters in num_char...
		                num = num + char						#...separate out the number...
		        try:
					zval = num									# ...and name it zval.
					zval = float(zval)							# converting zval from string to float
					mz = modz(zval)								# Call modz to get the deviation correction for the given zval
		        except ValueError:
		            pass

		    if token.startswith("F"):			#if it starts with the character 'F'...
		        num = ""
		        for char in token:
		            # print(char)
		            if char.isdigit() or (char in num_char):	#...and	also includes either a digit or one of the characters in num_char...
		                num = num + char						#...separate out the number...
		        try:
					fval = num									# ...and name it fval.
					mz = str(mz)
					zval = str(zval)								#convert mz back to string
					s = "G1 Z" + mz + " F" + fval				#Compose a new string to replace what was there before...
					print s										#...and print it (to the same line in the file)

		        except ValueError:
		            pass
	else:
		print line,				#Any other lines that don't include 'Z' should be reprinted what was already there. This is a catch all that might not do anything.
