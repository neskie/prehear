#!/bin/sh

# Prehead installation script 

echo "Installing to the rythmbox plugin directory (~/.gnome2/rhythmbox/plugins/)"
mkdir -p ~/.gnome2/rhythmbox/plugins/prehear
cp *.py ~/.gnome2/rhythmbox/plugins/prehear
cp *.rb-plugin ~/.gnome2/rhythmbox/plugins/prehear

echo "Installation finished
