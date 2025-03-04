from pyamaze import maze, COLOR, agent, textLabel
m=maze()
m.CreateMaze()

a = agent(m, 5, 5, filled=True, color = COLOR.red, footprints=True)
b = agent(m, 5, 6, filled=True, color = COLOR.yellow, footprints=True)

l = textLabel(m, 'Total Cells', m.rows*m.cols)

m.tracePath({a:m.path, b:m.path})
m.run()