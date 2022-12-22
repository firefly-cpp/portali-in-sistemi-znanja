#!/bin/bash

magenta='\033[0;35m'
clear='\033[0m'

echo -e "Running ${magenta}preprocessing${clear}"
cd priprava-podatkov/pandas/
for f in *.py; do python "$f" | grep Traceback ; done
cd ../..
echo -e "Running ${magenta}nature-inspired algorithms${clear}"
cd algoritmi-po-vzorih-iz-narave/
for f in *.py; do python "$f" | grep Traceback ; done
cd ..
echo -e "Running ${magenta}classification${clear}"
cd klasifikacija
for f in *.py; do python "$f" | grep Traceback ; done
cd ..
echo -e "Running ${magenta}classification 2${clear}"
cd kakovost-klasifikacije
for f in *.py; do python "$f" | grep Traceback ; done
cd ..
echo -e "Running ${magenta}automl${clear}"
cd automl
for f in *.py; do python "$f" | grep Traceback ; done
echo "Done"
