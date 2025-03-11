from pyamaze import maze, agent, COLOR, textLabel
from tarry import Tarry
import time

def test_small_0():
    pass

def test_small_50():
    pass

def test_small_100():
    pass

def test_medium_0():
    pass

def test_medium_50():
    pass

def test_medium_100():
    pass

def test_big_0():
    pass

def test_big_50():
    pass

def test_big_100():
    pass

if __name__ == '__main__':

    # Set Variables
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
    num_of_agents = 3

    # Create Maze
    m = maze()
    m.CreateMaze(loopPercent=50)
    agents = [agent(m, shape='arrow', footprints=True, color=colors[i]) for i in range(num_of_agents)]

    # Execute the Tarry's Algorithm
    start_time = time.time()
    paths = Tarry(m, num_of_agents)
    end_time = time.time()
    
    # Visualize the agents moving in the maze
    m.tracePath({agents[i]:paths[i] for i in range(num_of_agents)})
    l1 = textLabel(m, 'Total Path', sum([len(p) for p in paths.values()]))
    l2 = textLabel(m, 'Total Time', f"{end_time - start_time:.6f}s")
    m.run()