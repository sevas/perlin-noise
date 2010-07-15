#!/bin/sh


echo "Generating graph for $1"

STATSFILE="$1.profile"
DOTFILE="$1.dot"
OUTFILE="$1.png"

echo "--- $STATSFILE -> $DOTFILE "
gprof2dot -f pstats -o $DOTFILE  $STATSFILE
echo "--- $DOTFILE -> $OUTFILE"
dot -Tpng -o $OUTFILE $DOTFILE
rm $DOTFILE