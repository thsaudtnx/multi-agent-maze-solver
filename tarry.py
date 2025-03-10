from pyamaze import maze, agent, COLOR, textLabel
import random
import time

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

def Tarry(m, num_of_agents):
    start = (m.rows, m.cols)
    end = (1, 1)

    # Create agents
    dead_end = []
    paths = {i: [start] for i in range(num_of_agents)}
    frontier = [(i, start) for i in range(num_of_agents)]
    explored = {i : [start] for i in range(num_of_agents)}
    total_explored = [start]

    while frontier:

        print(f"frontier: {frontier}")
        print(f"total explored: {total_explored}")
        
        cur_agent_idx, cur_location = frontier.pop(0)
        
        if cur_location == end:
            continue
        
        not_explored_next_location = []
        possible_next_location = []

        for d in 'ESNW':
            if m.maze_map[cur_location][d] == 1:
                if d == 'E':
                    next_location = (cur_location[0],cur_location[1]+1)
                elif d=='W':
                    next_location=(cur_location[0],cur_location[1]-1)
                elif d=='N':
                    next_location=(cur_location[0]-1,cur_location[1])
                elif d=='S':
                    next_location=(cur_location[0]+1,cur_location[1])

                # not explored next location
                if next_location not in total_explored:
                    possible_next_location.append(next_location)
                # explored by other agents
                elif next_location not in explored[cur_agent_idx]:
                    not_explored_next_location.append(next_location)

        print(f"possible next location: {possible_next_location}")
        print(f"not explored next location: {not_explored_next_location}")
        print(f"Current Agent Explored: {explored[cur_agent_idx]}")
        print(f"Current Agent paths: {paths[cur_agent_idx]}")
        print("----------------------------")

        # If there are several such cells, the agent should choose one arbitrarily
        if possible_next_location:
            frontier.append((cur_agent_idx, possible_next_location[0]))
            explored[cur_agent_idx].append(possible_next_location[0])
            total_explored.append(possible_next_location[0])
            paths[cur_agent_idx].append(possible_next_location[0])
        
        # If all the locations has been traveled by other agents, the agent should prefer to move to a cell that has not been traveled by it.
        elif not_explored_next_location:
            frontier.append((cur_agent_idx, not_explored_next_location[0]))
            explored[cur_agent_idx].append(not_explored_next_location[0])
            paths[cur_agent_idx].append(not_explored_next_location[0])
        
        # If all the possible directions have already been traveled by the agent, 
        # or if the agent has reached a dead-end, 
        # the agent should retreat until a cell that meets one of the previous conditions.
        else:
            if cur_location not in dead_end:            
                dead_end.append(cur_location)
            prev_location_idx = paths[cur_agent_idx].index(cur_location) - 1
            prev_location = paths[cur_agent_idx][prev_location_idx]
            frontier.append((cur_agent_idx, prev_location))
            paths[cur_agent_idx].append(prev_location)
                
    print(f"Dead End: {dead_end}")
    print(f"Paths: {paths}")
    return paths

if __name__ == '__main__':

    # Set Variables
    colors = [COLOR.blue, COLOR.green, COLOR.cyan]
    num_of_agents = 1

    # Create Maze
    m = maze()
    m.CreateMaze(loopPercent=50)
    agents = [agent(m, footprints=True, filled=True, color=colors[i]) for i in range(num_of_agents)]

    # Execute the Tarry's Algorithm
    start_time = time.time()
    paths = Tarry(m, num_of_agents)
    end_time = time.time()
    
    # Visualize the agents moving in the maze
    m.tracePath({agents[i]:paths[i] for i in range(num_of_agents)})
    l1 = textLabel(m, 'Total Path', sum([len(p) for p in paths.values()]))
    l2 = textLabel(m, 'Total Time', f"{end_time - start_time:.6f}s")
    m.run()
