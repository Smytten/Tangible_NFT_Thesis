#!/bin/bash

echo '(¯`·.¸¸.·´¯`·.¸¸.·´¯)'
echo   Initializing World
echo 
echo ENTER CURRENT PARTICIPENT
read -p 'Participent: ' user

python3 actuateWorld.py $user
python3 masterServer.py $user