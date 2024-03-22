process= $(cat /proc/$(xdotool getwindowpid $(xdotool getwindowfocus))/comm)
eval $process
