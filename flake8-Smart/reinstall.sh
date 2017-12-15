#!/bin/bash

UNINSTALL="sudo pip uninstall --yes flake8-Smart"
INSTALL="sudo pip install ."

if [ "$EUID" -ne 0 ]
  then echo "Please run as root (with sudo)"
  exit
fi


echo $UNINSTALL && eval $UNINSTALL

echo $INSTALL && eval $INSTALL

