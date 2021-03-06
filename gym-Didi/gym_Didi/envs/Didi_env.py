import gym
from gym import Env, spaces, error
from gym import utils
import networkx as nx


# Set global variables

num_nodes = 8 
num_actions = num_nodes + 2
node = 4

locs = [3, 6, 7]  # Nodes where the passenger can be picked up or dropped off
num_dest_idx = len(locs)
num_pass_idx = len(locs) + 1
num_states = num_nodes * num_dest_idx * num_pass_idx  # num_states = 96  8_nodes * 3_dest * (3 + 1)_pass_loc
done = False 
reward = 0


# Graph definition

points_list = [(0, 1), (1, 2), (1, 3), (2, 3), (1, 5), (2, 7), (4, 5), (5, 6)] 
G = nx.Graph()
G.add_edges_from(points_list)
pos = nx.spring_layout(G)
A = nx.to_numpy_matrix(G, nodelist = [0, 1, 2, 3, 4, 5, 6, 7]) 



class Azione(object): 

  def __init__(self): 
      pass

  def take_action(self, action, pass_idx, new_pass_idx, dest_idx): 
     
      # We are writing a function to calculate the reward of every action and to complete
      # the episode when done = True. To do this we need action that is the return of choose_action

      # Defaults
      global new_node
      global reward
      global done
      done = False
          
      # Based on different actions   
      if action == num_nodes:  # Pick up
           if (new_pass_idx < len(locs) and new_node == locs[pass_idx]): # A number (n) between 0 and 2 means the passenger is in locs[n], 3 means the passenger is inside the Didi 
               new_pass_idx = len(locs)
               reward = -1    
           else:  # Pick up in a wrong node
                 reward = -10
      elif action == num_nodes + 1:  # Drop off
                if (new_node == locs[dest_idx]) and new_pass_idx == len(locs):
                                    new_pass_idx = dest_idx
                                    done = True
                                    reward = +1000
                else:  # Drop off in a wrong node
                      reward = -10
      else: # Action < 8
            reward = -1
            new_node = action

      # Update
      return self.encode(new_node, new_pass_idx, dest_idx), new_node, new_pass_idx, reward, done


  def encode(self, new_node, new_pass_idx, dest_idx):
        # (8), 3+1, 3
        m = new_node
        m *= num_pass_idx
        m += new_pass_idx
        m *= num_dest_idx
        m += dest_idx
        return m

  

class DidiEnv(gym.Env):  # We built our environment based on Gym library


  def __init__(self, seed = None):
     self.seed = seed
     self.action_space = spaces.Discrete(num_actions)
     self.observation_space = spaces.MultiDiscrete([num_nodes, num_pass_idx, num_dest_idx])


  def step(self, action, pass_idx, new_pass_idx, dest_idx):
      
     # Return new_state, new_node, new_pass_idx, reward and done based on the results of Azione().take_action 
     
     self.pass_idx = pass_idx
     self.new_pass_idx = new_pass_idx
     self.dest_idx = dest_idx
     global new_state
     global new_node
     global reward
     global done
     new_state, new_node, new_pass_idx, reward, done = Azione().take_action(action, pass_idx, new_pass_idx, dest_idx)
     return  new_state, new_node, new_pass_idx, reward, done

  def reset(self, new_pass_idx, dest_idx):

      # Reset state, new_node, new_pass_idx, done, reward to the initial conditions 
      
      self.new_pass_idx = new_pass_idx
      self.dest_idx = dest_idx
      global new_node
      new_node = node       
      global state
      state = Azione().encode(new_node, new_pass_idx, dest_idx)
      global new_state
      new_state = Azione().encode(new_node, new_pass_idx, dest_idx)
      global reward
      reward = 0
      global done
      done = False
      return state, new_state, new_node, reward