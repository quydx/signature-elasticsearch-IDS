git add .
if [[ -v $1 ]];then 
    git commit -a -m "$1"
else
    git commit -a -m "update"
fi
git push -u origin master
