#!/bin/bash
HOST='fifoandlifo.fr'
USER='dev'
PASS='cpo$094y%'
TARGETFOLDER='/'
SOURCEFOLDER='./'
EXCLUDEPYCACHE='__pycache__' 
EXCLUDECODEMIRROR='static/assets/codemirror/'
EXCLUDEFONTAWESOME='static/assets/fontawesome/'
EXCLUDEHIGHLIGHT='static/assets/highlight/'
EXCLUDEGIT='.git/'
EXCLUDEGITLABCI='.gitlab-ci.yml' 
lftp -f "
open $HOST
user $USER $PASS
lcd $SOURCEFOLDER
mirror --reverse --delete --verbose --exclude=$EXCLUDEREG  --exclude-glob=$EXCLUDEMATHJAX --exclude-glob=$EXCLUDEPYCACHE --exclude-glob=$EXCLUDEHIGHLIGHT --exclude-glob=$EXCLUDEGIT --exclude-glob=$EXCLUDECODEMIRROR  --exclude-glob=$EXCLUDEFONTAWESOME --exclude-glob=$EXCLUDEDIRECTORY --exclude-glob=$EXCLUDEDROPBOX --exclude-glob=$EXCLUDEDSSTORE --exclude-glob=$EXCLUDECORRECTION --parallel=4  $SOURCEFOLDER $TARGETFOLDER
bye
"