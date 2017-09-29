#!/bin/bash
# Dylan Rothfeld 09/29/2017
# Execute this to run 'imageObjectCounter.py' on the current directory
# Both 'imageObjectCounter.py' and 'runObjectCounter.sh' need to be
# in the targeted directory

echo "----------STARTING IMAGE_OBJECT_COUNTER----------"
for file in *;
  do
    python imageObjectCounter.py "$file"
  done
echo "----------FINISHED IMAGE_OBJECT_COUNTER----------"
