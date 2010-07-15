@ECHO off
ECHO Generating graph for %1%

@SET STATSFILE=%1%.profile
@SET DOTFILE=%1%.dot
@SET OUTFILE=%1%.png

gprof2dot -f pstats -o %DOTFILE%  %STATSFILE%
dot -Tpng -o %OUTFILE% %DOTFILE%
del %DOTFILE%