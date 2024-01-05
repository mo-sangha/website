#!/bin/bash

# This script will resize all images in the current directory to 800x800px and save them in the frontend/static folder as "photo-<filename>.jpg"

for file in *.png *.jpg; do 
  convert "$file" -resize 800x800^ -gravity center -extent 800x800 -quality 80 "../../static/photo-${file%.*}.jpg"; 
done
