git add .
if [[ -v $1 ]];then 
    echo "commit with message = $1"
else
    echo "commit with message = update"
    1="update"
fi
git commit -a -m "$1"
git push -u origin master
