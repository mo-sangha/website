#!/bin/bash

for file in *.png *.jpg; do 
  convert "$file" -resize 800x800^ -gravity center -extent 800x800 -quality 80 "../../static/photo-${file%.*}.jpg"; 
done
