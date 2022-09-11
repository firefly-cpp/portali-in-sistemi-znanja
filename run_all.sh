#!/bin/bash

magenta='\033[0;35m'
clear='\033[0m'

echo -e "Running ${magenta}preprocessing${clear}"
for f in priprava-podatkov/pandas/*.py; do python "$f"; done
echo -e "Running ${magenta}nature-inspired algorithms${clear}"
for f in algoritmi-po-vzorih-iz-narave/*.py; do python "$f"; done
