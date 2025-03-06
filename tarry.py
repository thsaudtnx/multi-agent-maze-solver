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

    r = 30

    while frontier and r > 0:

        r -= 1

        print(f"frontier: {frontier}")
        print(f"total explored: {total_explored}")
        
        current_agent_idx, current_location = frontier.pop(0)

        others_explored_next_location = []
        possible_next_location = []
        possible_prev_location = []
        
        if current_location == end:
            continue
        
        for d in 'ESNW':
            if m.maze_map[current_location][d] == 1:
                if d == 'E':
                    next_location = (current_location[0],current_location[1]+1)
                elif d=='W':
                    next_location=(current_location[0],current_location[1]-1)
                elif d=='N':
                    next_location=(current_location[0]-1,current_location[1])
                elif d=='S':
                    next_location=(current_location[0]+1,current_location[1])

                # dead end
                if next_location in dead_end:
                    continue

                # check which agent explored the possible next location
                if next_location in total_explored:
                    if next_location in explored[current_agent_idx]:
                        possible_prev_location.append(next_location)
                    else:
                        others_explored_next_location.append(next_location)
                # The agent should move to cells that have not been traveled by any agent
                else:
                    possible_next_location.append(next_location)

        print(f"possible next location: {possible_next_location}")
        print(f"possible prev location: {possible_prev_location}")
        print(f"others explored next location: {others_explored_next_location}")

        # If there are several such cells, the agent should choose one arbitrarily
        if possible_next_location:
            frontier.append((current_agent_idx, possible_next_location[0]))
            explored[current_agent_idx].append(possible_next_location[0])
            total_explored.append(possible_next_location[0])
            paths[current_agent_idx].append(possible_next_location[0])
        else:
            # If there is no cell that has not been traveled by an agent, the agent should prefer to move to a cell that has not been traveled by it.
            if others_explored_next_location:
                frontier.append((current_agent_idx, others_explored_next_location[0]))
                paths[current_agent_idx].append(others_explored_next_location[0])
                explored[current_agent_idx].append(others_explored_next_location[0])
            # If all the possible directions have already been traveled by the agent, or if the agent has reached a dead-end, the agent should retreat until a cell that meets one of the previous conditions.
            else:
                # When retreating, mark the cells retreated from as “dead end”.
                dead_end.append(current_location)
                frontier.append((current_agent_idx, possible_prev_location[0]))
                paths[current_agent_idx].append(possible_prev_location[0])
                

    print(paths)
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
    l = textLabel(m, 'Total Path', sum([len(p) for p in paths.values()]))
    l = textLabel(m, 'Total Time', f"{end_time - start_time:.6f}s")
    m.run()
