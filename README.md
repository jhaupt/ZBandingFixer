This script will imprint a periodic structure onto the motion of the Z axis of a 3D printer to compensate for incosistent (periodic) Z motion.

It will ingest the newest .gcode file in the same directory as itself, modify all the Z movements according to variables defined in the script, and write it back to the same file.

It will NOT do anything for Z wobble, only Z banding caused by z-axis movement error.For clarity, wobble is a periodic shift in layers due to lateral movement of the stage, wheras the banding referred to here is a periodic dilation in layers.

By Justine Haupt
