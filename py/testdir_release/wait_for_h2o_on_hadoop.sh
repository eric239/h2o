
echo ""
echo "Have to wait until h2o_one_node is available from the cloud build. Deleted it above."
echo "spin loop here waiting for it."

count=0
rm -fr h2o_one_node
while [ ! -f h2o_one_node ]
do
    sleep 5
    set +e
    echo "$REMOTE_SCP $REMOTE_USER:$REMOTE_HOME/h2o_one_node ."
    $REMOTE_SCP $REMOTE_USER:$REMOTE_HOME/h2o_one_node .
    set -e
    (( count++ ))
    if [ $count == 100 ]
    then
        echo "h2o didn't start on hadoop, after waiting 500 secs"
    fi
done
ls -lt h2o_one_node

