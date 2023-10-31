# !/bin/bash
#./run_orthofinder.sh 

 

 cp *.faa OrthoFinder  
 cd OrthoFinder/
 mkdir  Sequences 
 cp *.faa Sequences 
./orthofinder -f    Sequences 