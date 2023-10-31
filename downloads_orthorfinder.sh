# !/bin/bash  
# ./downloads_orthofinder.sh

# # this script automate   download aand testing of the installation fo orthofinder
#Written by: Rodrigo Alex Henríquez Arancibia 
# Date Written: October  24,2023


#!/bin/bash  
#Download orthofinder
from os import chmod


wget https://github.com/davidemms/OrthoFinder/releases/latest/download/OrthoFinder.tar.gz
tar -xzf OrthoFinder.tar.gz 
cd OrthoFinder/

# testing orthofinder 
chmod +x orthofinder 
./orthofinder -h 

./orthofinder -f ExampleData
