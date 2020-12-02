# Reinforcement Learning of a taxi on a graph environment

Description: 
We build a graph with a prefixed number of nodes (in our case 8). Our Didi (it's like an Uber) has to pick up and to drop off a passenger in specified nodes. We defined three different passenger locations and destinations. The Didi pays -1 for each allowed step, -10 if the action is forbidden (for example to pick up or to drop off the passenger in a wrong node) and it receives a positive reward (+1000) and the event ends only if it drops off the passenger in the correct node. The training of the Didi is based on nine different combinations (there are three different passenger locations and destinations).
Observations The number of states (96) is a combination of the num_nodes (8), the num_pass_idx (4) and the num_dest_idx (3). The num_pass_idx is 4 because there are 3 possible locations where to pick up the passenger and the fourth case represents the possibility that the passenger is inside the Didi.


Action: 
The number of actions is equal to num_nodes + 2. Notably the actions are to pick up, to drop off and all the possible transitions towards a particular node.
In this specific example:
action 0 means to go to the 0 node
action 1 means to go to the 1 node
...
action 7 means to go to the 7 node
action 8 is to pick up
action 9 is to drop off


Render:
yellow: passenger position
blue: destination
green: empty Didi
red: full Didi
orange: pick up or drop off in wrong nodes


Rewards:
The reward depends on the action
-1 for each allowed action
-10 if drop off or pick up are executed in wrong nodes
+1000 if the Didi drops off the passengerse in the correct dest_node.


A more complex problem was solved with Deep Reinforcement Learning, check out my repositories for more informations.

I developed this project with the help of two colleagues. If you need any help, contact us: 
vanessa.staderini@gmail.com 
tommaso3d@gmail.com 
95vittoriar@gmail.com
