#!/bin/bash
ver=`/bin/uname -m`
if [[ $ver == *64* ]]
then
  echo "64-bit version";
  scr="Miniconda3-3.3.0-Linux-x86_64.sh"
else
  echo "32-bit version";
  scr="Miniconda3-3.3.0-Linux-x86.sh"
fi
wget "http://repo.continuum.io/miniconda/"$scr
bash $scr
