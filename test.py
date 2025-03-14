from pyamaze import maze
from tarry import Tarry
import pandas as pd
import matplotlib.pyplot as plt

def create_maze(maze_size, loopPercent):
    m = maze(maze_size, maze_size)
    m.CreateMaze(loopPercent=loopPercent, saveMaze=True)
    m._win.destroy()

def plot_results(df):
    """Plots the impact of number of agents on total time using the best sensor length."""
    plt.figure(figsize=(10, 6))
    plt.plot(df["Number of Agents"], df["Total Time (seconds)"], marker='o', linestyle='-', label="Best Sensor Length")

    # Annotate the best sensor length for each agent count
    for _, row in df.iterrows():
        plt.annotate(f"{int(row['Sensor Length'])}", 
                     (row["Number of Agents"], row["Total Time (seconds)"]),
                     textcoords="offset points", xytext=(0, 10), ha='center')

    # Labels and Title
    plt.xlabel("Number of Agents")
    plt.ylabel("Total Time (seconds)")
    plt.title("Impact of Number of Agents on Total Time (Using Best Sensor Length)")
    plt.xticks(df["Number of Agents"]) 
    plt.grid(True, linestyle="--", alpha=0.7)

    # Show plot
    plt.legend(title="Best Sensor Length")
    plt.show()

def test_maze(maze_size, loop):

    # Set the range for number of agents and sensor lengths
    agents = [i for i in range(1, maze_size+1, maze_size//10)]
    sensors = [i for i in range(1, maze_size+1, maze_size//10)]

    best_sensor_lengths = {}
    results = []

    print(f"--- Test Maze of {maze_size}, {loop} ---")

    for agent in agents:
        print(f"Number of Agents: {agent}")
        best_time = float("inf")
        best_sensor = None
        best_total_path = None

        for sensor in sensors:

            m = maze(maze_size, maze_size)
            m.CreateMaze(loadMaze=f"maze/maze_{maze_size}_{loop}.csv", theme='light')

            paths, total_time, total_path = Tarry(m, agent, sensor)
            m._win.destroy()

            if total_time < best_time:
                best_time = total_time
                best_sensor = sensor
                best_total_path = total_path

            print(f"Sensor Length: {sensor}")
            print(f"Total Time: {total_time}")
            print(f"Total Path: {total_path}")
            print()
        
        results.append({
            "Number of Agents": agent,
            "Sensor Length": best_sensor,
            "Total Time (seconds)": best_time,
            "Total Path": best_total_path
        })

        best_sensor_lengths[agent] = best_sensor

    # Convert results to a DataFrame
    df = pd.DataFrame(results)
    plot_results(df)

def simulate_maze(maze_size, loop, agent, sensor):

    m = maze(maze_size, maze_size)
    m.CreateMaze(loadMaze=f"maze/maze_{maze_size}_{loop}.csv", theme='light')
    paths, total_time, total_path = Tarry(m, agent, sensor)
    m.tracePath(paths, delay=100)
    m.run()

    print(f"--- Simulation for maze_{maze_size}_{loop} ---")
    print(f"Number of Agent: {agent}")
    print(f"Sensor Length: {sensor}")
    print(f"Total Time: {total_time}")
    print(f"Total Path: {total_path}")
    

if __name__ == '__main__':
    #create_maze(10, 0)
    #create_maze(10, 50)
    #create_maze(10, 100)
    #create_maze(20, 0)
    #create_maze(20, 50)
    #create_maze(20, 100)
    #create_maze(30, 0)
    #create_maze(30, 50)
    #create_maze(30, 100)
    
    #test_maze(10, 0)
    #test_maze(10, 50)
    test_maze(10, 100)