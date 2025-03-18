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
        best_time = float("inf")
        best_sensor = None
        best_total_path = None

        print(f"Number of Agents: {agent}")

        for sensor in sensors:

            m = maze(maze_size, maze_size)
            m.CreateMaze(loadMaze=f"maze/maze_{maze_size}_{loop}.csv", theme='light')

            paths, total_time, total_path, first_solver_time = Tarry(m, agent, sensor)
            m._win.destroy()

            if total_time < best_time:
                best_time = total_time
                best_sensor = sensor
                best_total_path = total_path

            print(f"Sensor Length: {sensor}")
            print(f"Total Time: {total_time}")
            print(f"Total Path: {total_path}")
            print(f"First Solver Time: {first_solver_time}")
            print(f"")
        
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

    # Save table as CSV
    #table_filename = f"table_{maze_size}_{loop}.csv"
    #df.to_csv(table_filename, index=False)
    #print(f"Results saved as {table_filename}")
    
def simulate_maze(maze_size, loop, agent, sensor):

    m = maze(maze_size, maze_size)
    m.CreateMaze(loadMaze=f"maze/maze_{maze_size}_{loop}.csv", theme='light')
    paths, total_time, total_path, first_solver_time = Tarry(m, agent, sensor)
    m.tracePath(paths, delay=100)
    m.run()
    
def show_maze(maze_size, loop):
    m = maze(10, 10)
    m.CreateMaze(loadMaze=f"maze/maze_{10}_{100}.csv", theme='light')
    m.run()

if __name__ == '__main__':
    # Maze is already created so no need to run these lines.
    #create_maze(10, 0)
    #create_maze(10, 50)
    #create_maze(10, 100)

    # Shows the maze
    #show_maze(10, 0)
    #show_maze(10, 50)
    #show_maze(10, 100)
    
    # Show the result of agents with graphs
    #test_maze(10, 0)
    #test_maze(10, 50)
    #test_maze(10, 100)

    # Agent Simulation
    #simulate_maze(10, 0, 1, 6)
    #simulate_maze(10, 0, 2, 1)
    #simulate_maze(10, 0, 3, 1)
    #simulate_maze(10, 0, 4, 1)
    #simulate_maze(10, 0, 5, 2)
    #simulate_maze(10, 0, 6, 1)
    #simulate_maze(10, 0, 7, 1)
    #simulate_maze(10, 0, 8, 1)
    #simulate_maze(10, 0, 9, 1)
    #simulate_maze(10, 0, 10, 1)

    #simulate_maze(10, 50, 1, 7)
    #simulate_maze(10, 50, 2, 1)
    #simulate_maze(10, 50, 3, 1)
    #simulate_maze(10, 50, 4, 1)
    #simulate_maze(10, 50, 5, 1)
    #simulate_maze(10, 50, 6, 1)
    #simulate_maze(10, 50, 7, 1)
    #simulate_maze(10, 50, 8, 1)
    #simulate_maze(10, 50, 9, 1)
    #simulate_maze(10, 50, 10, 1)

    #simulate_maze(10, 100, 1, 6)
    #simulate_maze(10, 100, 2, 1)
    #simulate_maze(10, 100, 3, 2)
    #simulate_maze(10, 100, 4, 1)
    #simulate_maze(10, 100, 5, 1)
    #simulate_maze(10, 100, 6, 1)
    #simulate_maze(10, 100, 7, 1)
    #simulate_maze(10, 100, 8, 1)
    #simulate_maze(10, 100, 9, 1)
    simulate_maze(10, 100, 10, 1)

    
