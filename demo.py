from pyamaze import maze, COLOR, agent, textLabel
m=maze(5, 5)
m.CreateMaze()

a = agent(m, filled=True, footprints=True)

l = textLabel(m, 'Total Cells', m.rows*m.cols)
print(m.maze_map)
m.tracePath({a:m.path})
m.run()