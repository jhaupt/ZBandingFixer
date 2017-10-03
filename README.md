This script will imprint a periodic structure onto the motion of the Z axis of a 3D printer to compensate for incosistent (periodic) Z motion.

It will ingest the newest .gcode file in the same directory as itself, modify all the Z movements according to variables defined in the script, and write it back to the same file.

The shape of the periodic structure is defined by an easy-to-read Fourier Series. Delete all but the first term to get a sine wave.

This will NOT do anything for Z wobble; only Z banding caused by z-axis movement error specifically. There are many possible sources of banding, so be sure yours is caused by periodic motion in the Z axis before considering applying this script. For clarity, wobble is a periodic shift in layers due to lateral movement of the stage, wheras the banding referred to here is a periodic dilation in layers.

Use with extreme care. Review modified gcode by eye until confident in its use. This code has only been tested with gcode generated by Simplify3D. I can not be held responsible for damage caused a printer through the use of this script.

By Justine Haupt
