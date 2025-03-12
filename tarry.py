import math
from pyamaze import agent, COLOR

"""
Tarry's Algorithm
1) The agent should move to cells that have not been traveled by any agent.
2) If there are several such cells, the agent should choose one arbitrarily.
3) If there is no cell that has not been traveled by an agent, the agent should prefer to move to a cell that has
not been traveled by it.
4) If all the possible directions have already been traveled by the agent, or if the agent has reached a dead-end,
the agent should retreat until a cell that meets one of the previous conditions.
5) All the steps should be logged by the agent in its history.
6) When retreating, mark the cells retreated from as “dead end”.
"""

# Set Global Variables
colors = [
    COLOR.black, 
    COLOR.blue, 
    COLOR.cyan, 
    COLOR.dark, 
    COLOR.green, 
    COLOR.light, 
    COLOR.red, 
    COLOR.yellow
]
        
class Agent:

    def __init__(self, m, agent_idx, sensor_len = 5):
        self.agent_idx = agent_idx
        self.m = m
        self.agent = agent(m, shape='arrow', footprints=True, color=colors[agent_idx])
        self.dead_end = []
        start = (m.rows, m.cols)
        self.path = [start] * (agent_idx + 1)
        self.explored = [start]
        self.total_explored = [start]
        self.solver_agent_path = []
        self.sensor_len = sensor_len
        self.nearby_agents_location = []
    
    def find_nearby_agents(self, agents):
        current_x, current_y = self.path[-1]
        nearby_agents = []

        for agent in agents:
            
            agent_x, agent_y = agent.path[-1]
            distance = math.sqrt((agent_x - current_x) ** 2 + (agent_y - current_y) ** 2)

            if distance <= self.sensor_len:
                nearby_agents.append(agent)
        
        return nearby_agents
    
    def communicate_with_nearby_agents(self, nearby_agents):
        # update explored cells and dead end from the other agents
        nearby_agents_location = []
        for agent in nearby_agents:

            nearby_agents_location.append(agent.path[-1])

            for de in agent.dead_end:
                if de not in self.dead_end:
                    self.dead_end.append(de)
                
            for te in agent.total_explored:
                if te not in self.total_explored:
                    self.total_explored.append(te)
        
            if not self.solver_agent_path and agent.path[-1] == (1, 1):
                self.solver_agent_path = agent.path
    
    def get_nearby_agents_location(self, next_location, nearby_agents):
        for agent in nearby_agents:
            if agent.path[-1] == next_location:
                return True
        return False
    
    def move(self):
        current_location = self.path[-1]

        # if current agent already reach the goal
        if current_location == (1, 1):
            return
        
        # if current agent is following the solver agent path
        if current_location in self.solver_agent_path:
            next_location_idx = len(self.solver_agent_path) - list(reversed(self.solver_agent_path)).index(current_location)
            next_location = self.solver_agent_path[next_location_idx]
            if next_location not in self.explored:
                self.explored.append(next_location)
            self.path.append(next_location)
            return
        
        # distinguish cells which only visited by this agent or the others
        not_explored_by_this_agent_location = []
        not_explored_by_all_agent_location = []

        for d in 'ESNW':
            if self.m.maze_map[current_location][d] == 1:
                if d == 'E':
                    next_location = (current_location[0],current_location[1]+1)
                elif d=='W':
                    next_location=(current_location[0],current_location[1]-1)
                elif d=='N':
                    next_location=(current_location[0]-1,current_location[1])
                elif d=='S':
                    next_location=(current_location[0]+1,current_location[1])

                # all ther agents have not explored the location
                if next_location not in self.total_explored:
                    not_explored_by_all_agent_location.append(next_location)
                # explored by other agents but not by this agent
                elif next_location not in self.explored:
                    not_explored_by_this_agent_location.append(next_location)
        
        # If there are several such cells, the agent should choose one arbitrarily
        if not_explored_by_all_agent_location:
            for next_location in not_explored_by_all_agent_location:
                if next_location not in self.nearby_agents_location:
                    self.explored.append(next_location)
                    self.total_explored.append(next_location)
                    self.path.append(next_location)
                    break
        
        # If all the locations has been traveled by other agents, the agent should prefer to move to a cell that has not been traveled by it.
        elif not_explored_by_this_agent_location:
            for next_location in not_explored_by_this_agent_location:
                if next_location not in self.nearby_agents_location:
                    self.explored.append(next_location)
                    self.path.append(next_location)
                    break
        
        # If all the possible directions have already been traveled by the agent, 
        # or if the agent has reached a dead-end, 
        # the agent should retreat until a cell that meets one of the previous conditions.
        else:
            if current_location not in self.dead_end:            
                self.dead_end.append(current_location)
            prev_location_idx = self.path.index(current_location) - 1
            prev_location = self.path[prev_location_idx]
            self.path.append(prev_location)

def is_solved(agents):
    for agent in agents:
        if agent.path[-1] != (1, 1):
            return False
    
    return True


def Tarry(m, num_of_agents):

    paths = {}
    frontier = [Agent(m, agent_idx) for agent_idx in range(num_of_agents)]
    
    while frontier:

        agent = frontier.pop(0)
        print(f"--- Agent_{agent.agent_idx} ---")
        current_location = agent.path[-1]
        print(f"Current Location: {agent.path[-1]}")
        if current_location == (1, 1):
            frontier.append(agent)
            continue
        
        # agent process
        nearby_agents = agent.find_nearby_agents(frontier)
        print(f"Nearby Agents: {[agent.agent_idx for agent in nearby_agents]}")
        agent.communicate_with_nearby_agents(nearby_agents)
        agent.move()

        # update the total paths
        paths[agent] = agent.path

        locations = {f"Agent_{agent.agent_idx}": path[-1] for agent, path in paths.items()}

        print(f"Next Locations: {locations}")
        print("-----------------------")

        frontier.append(agent)

        # check if all the agents reach the goal
        if is_solved(frontier):
            break

    p = {agent.agent : path for agent, path in paths.items()}
    return p
