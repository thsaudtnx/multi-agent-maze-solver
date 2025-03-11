from pyamaze import maze, agent, COLOR, textLabel
from tarry import Tarry
import time

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

def create_maze():
    # Execute one by one
    # small
    m = maze(10, 10)
    m.CreateMaze(loopPercent=0, saveMaze=True)
    m.CreateMaze(loopPercent=50, saveMaze=True)
    m.CreateMaze(loopPercent=100, saveMaze=True)

    # medium
    m = maze(50, 50)
    m.CreateMaze(loopPercent=0, saveMaze=True)
    m.CreateMaze(loopPercent=50, saveMaze=True)
    m.CreateMaze(loopPercent=100, saveMaze=True)

    # large
    m = maze(100, 100)
    m.CreateMaze(loopPercent=0, saveMaze=True)
    m.CreateMaze(loopPercent=50, saveMaze=True)
    m.CreateMaze(loopPercent=100, saveMaze=True)
    
def testing(m, num_of_agents):
    agents = [agent(m, shape='arrow', footprints=True, color=colors[i]) for i in range(num_of_agents)]

    # Execute the Tarry's Algorithm
    start_time = time.time()
    paths = Tarry(m, num_of_agents)
    end_time = time.time()
    
    # Visualize the agents moving in the maze
    m.tracePath({agents[i]:paths[i] for i in range(num_of_agents)})
    l1 = textLabel(m, 'Total Path', sum([len(p) for p in paths.values()]))
    l2 = textLabel(m, 'Total Time', f"{end_time - start_time:.6f}s")
    l3 = textLabel(m, 'Total Cells', m.rows*m.cols)

    m.run()

def test_small_0(num_of_agents):
    m = maze(10, 10)
    m.CreateMaze(loadMaze="/Users/sonmyungsoo/Downloads/multi-agent-maze-solver/maze/small_0.csv", theme='light')
    testing(m, num_of_agents)

def test_small_50(num_of_agents):
    # Create Maze
    m = maze(10, 10)
    m.CreateMaze(loadMaze="/Users/sonmyungsoo/Downloads/multi-agent-maze-solver/maze/small_50.csv", theme='light')
    testing(m, num_of_agents)

def test_small_100(num_of_agents):
    # Create Maze
    m = maze(10, 10)
    m.CreateMaze(loadMaze="/Users/sonmyungsoo/Downloads/multi-agent-maze-solver/maze/small_100.csv", theme='light')
    testing(m, num_of_agents)

def test_medium_0(num_of_agents):
    # Create Maze
    m = maze(50, 50)
    m.CreateMaze(loadMaze="/Users/sonmyungsoo/Downloads/multi-agent-maze-solver/maze/medium_0.csv", theme='light')
    testing(m, num_of_agents)

def test_medium_50(num_of_agents):
    # Create Maze
    m = maze(50, 50)
    m.CreateMaze(loadMaze="/Users/sonmyungsoo/Downloads/multi-agent-maze-solver/maze/medium_50.csv", theme='light')
    testing(m, num_of_agents)

def test_medium_100(num_of_agents):
    # Create Maze
    m = maze(50, 50)
    m.CreateMaze(loadMaze="/Users/sonmyungsoo/Downloads/multi-agent-maze-solver/maze/medium_100.csv", theme='light')
    testing(m, num_of_agents)

def test_large_0(num_of_agents):
    # Create Maze
    m = maze(100, 100)
    m.CreateMaze(loadMaze="/Users/sonmyungsoo/Downloads/multi-agent-maze-solver/maze/large_0.csv", theme='light')
    testing(m, num_of_agents)

def test_large_50(num_of_agents):
    # Create Maze
    m = maze(100, 100)
    m.CreateMaze(loadMaze="/Users/sonmyungsoo/Downloads/multi-agent-maze-solver/maze/large_50.csv", theme='light')
    testing(m, num_of_agents)

def test_large_100(num_of_agents):
    # Create Maze
    m = maze(100, 100)
    m.CreateMaze(loadMaze="/Users/sonmyungsoo/Downloads/multi-agent-maze-solver/maze/large_100.csv", theme='light')
    testing(m, num_of_agents)

if __name__ == '__main__':
    #create_maze()
    test_small_0(2)
    #test_small_50(2)
    #test_small_100(2)
    #test_medium_0(2)
    #test_medium_50(2)
    #test_medium_100(2)
    #test_large_0(2)
    #test_large_50(2)
    #test_large_100(2)