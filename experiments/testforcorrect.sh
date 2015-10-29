echo "greedy change diff:"
python changegreedy.py correct
diff correctchange.txt correctmanualgreedy.txt
echo "---------------------"

echo "dp change diff:"
python changedp.py correct
diff correctchange.txt correctmanual.txt
echo "---------------------"

echo "slow change diff:"
python changeslow.py correct
diff correctchange.txt correctmanual.txt
echo "---------------------"
