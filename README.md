This script will imprint a periodic structure onto the motion of the Z axis of a 3D printer to compensate for incosistent (periodic) Z motion.

It will ingest the newest .gcode file in the same directory as itself, modify all the Z movements according to variables defined in the script, and write it back to the same file.

The shape of the periodic structure is defined by an easy-to-read Fourier Series. Delete all but the first term to get a sine wave.

This will NOT do anything for Z wobble; only Z banding caused by z-axis movement error specifically. There are many possible sources of banding, so be sure yours is caused by periodic motion in the Z axis before considering applying this script. For clarity, wobble is a periodic shift in layers due to lateral movement of the stage, wheras the banding referred to here is a periodic dilation in layers.

Use with extreme care. Review modified gcode by eye until confident in its use. This code has only been tested with gcode generated by Simplify3D. I can not be held responsible for damage caused a printer through the use of this script.

Use:

-It will convert the most recently created file with a .gcode extension in the same directory. There are no prompts; changes must be made in the script.

-If you use it it will be absolutely necessary to edit the correction parameters to suit. Read the comments.

-I use Simplify3D; it's untested with other slicers' gcode.

-There are many many causes of horizontal banding and this can only fix one, so confidence is needed in that regard.

-If you have a drop indicator, I recommend using it and logging the as-measured bed deviation every .01mm to determine the correct amplitude and amplitude center for the script. 

-The phase of the correction function is important and I found I needed to find it by trial and error. After the first print, I could guess at the next phase to try by eye, but once close I ran a bunch of test cubes at .1mm offsets in phase, and then .05mm offsets, and picked the best one.

-The shape of the correction function is the trickiest. My banding has a profile somewhere between a sine wave and a sawtooth pattern, so I composed the correction function with a Fourier Series to do what I want. One can add more terms by copying and pasting and editing coefficients as needed, or commenting out, but if unsure the best starting point is probably a good ole sine function. There are instructions in the comments, but basically you'd leave just the first term in the function uncommented to get a sine. Also, it will plot the function for you when trying to get the shape right.


By Justine Haupt
