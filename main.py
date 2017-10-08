import tkinter as tk
import numpy as np

class Grid(tk.canvas):
  '''Grid object hold nodes'''
  def __init__(self, parent, rows, columns, *args, **kwargs):
    tk.Canvas.__init__(self, parent, *args, **kwargs)
    self.parent = parent
    self.grid_ary = np.empty((rows,columns), dtype=object) #holds the nodes on grid
    self.ngx, self.ngy, self.ndm, self.adjx, self.adjy = 0,0,0,0,0 #space between nodes, diameter of node, adjustment
    #self.bind("<Configure>", self.scale) #to scale

  def populate():
    #fills the grid with nodes
    for (r, c), n in np.ndenumerate(self.grid_ary):
    	self.grid[r,c] = Node(r, c, True)

	def drawNodes():
    #calls the draw function on each node
    for (r, c), n in np.ndenumerate(self.grid_ary):
    	n.draw(self) #calls draw but passes in self because to draw Nodes on self
    print("drawing Nodes")

  def updateNodes(): #doesn't draw but update them
		for (r, c), n in np.ndenumerate(self.gridAry):
      self.coords(n.name, n.pos) #takes canvas object tag and changes its position
      #self.coords(n.name+'text', n.center)

class Node:
  def __init__(self, x, y, passable):
    n.name = "%d,%d"%(x,y) #string of Node coordinates
    self.position = [x,y]
    self.passable = passable #boolean
    self.color = 'white' if passable = true else 'black'

  def draw(self, canvas, coords):
    canvas.create_oval(coords, self.color, tags=[n.name])

  def invert_passable(self):
    self.passable = not self.passable
    self.color = 'white' if passable = true else 'black'

  def r_passable(self):
    return self.passable

  def r_position(self):
    return self.postion

  def r_color(self):
    return self.color

class Navigator():
  self.options = ['djiskstra_navigate']
  def __init__(start, end):
    self.start_node = start
    self.end_node = end

  def r_options(self):
    return self.options

  def djikstra_navigate():
    # implement djikstra navigation here
    
    # represent grid as a tree
    # if

if __name__ == '__main__':
  root = tk.Tk()
  gr = GridCanvas( root, 2, 3, width=500, height=500)
  gr.populate()
  gr.drawNodes()
  gr.pack(side="bottom", fill="both", expand=True)
    #pulldown menu
    variable = StringVar(root)
    navigation = Navigator.r_options()
    variable.set(navigation[0]) # default value
    w = apply(OptionMenu, (root, variable) + tuple(navigation))
    w.pack()
    mainloop()
