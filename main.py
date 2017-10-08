import numpy as np
import tkinter as tk

class GridCanvas(tk.Canvas):
    '''Grid object hold nodes'''
    def __init__(self, parent, rows, columns, *args, **kwargs):
        tk.Canvas.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.gridAry = np.empty((rows,columns), dtype=object)
        self.ngx, self.ngy, self.ndm, self.adjx, self.adjy = 0,0,0,0,0 #space between nodes, diameter of node, adjustment
        self.bind("<Configure>", self.scale)

    def populate(self):
        '''fill grid with nodes'''
        for (r, c), n in np.ndenumerate(self.gridAry):
            self.gridAry[r,c] = Node('%d, %d'% (r, c), 'pink', [self.adjx+ r*self.ngx,          self.adjy+ c*self.ngy,
                                                                self.adjx+ r*self.ngx +self.ndm, self.adjy+ c*self.ngy+self.ndm])

    def drawNodes(self, update=False):
        '''draws or update drawn nodes'''
        #set update to true if you want to update items not draw them
        if not update:
            for (r, c), n in np.ndenumerate(self.gridAry):
                self.create_oval(n.pos, fill=n.color, tags=[n.name])
                self.create_text(n.center, text=n.name, tags=[n.name+'text'])
        else:
            for (r, c), n in np.ndenumerate(self.gridAry):
                self.coords(n.name, n.pos)
                self.coords(n.name+'text', n.center)#[(self.adjx+r*self.ngx) + (self.ndm/2), (self.adjy+c*self.ngy) +(self.ndm/2)])
                #self.itemconfigure(n.name+'text', text=n.name)

    def scale(self, event):
        '''scales nodes'''
        #canvas.itemconfigure("event", text="event.width: %s" % event.width
        self.ngx, self.ngy = event.width/self.gridAry.shape[0], event.height/self.gridAry.shape[1]
        self.ndm = min(self.ngx, self.ngy)*0.50
        self.adjx, self.adjy = event.width*0.05, event.height*0.05
        #(event.width - (self.gridAry.shape[0]-1)*self.ngx+self.ndm) /2, (event.height - (self.gridAry.shape[1]-1)*self.ngy+self.ndm) /2
        #scaling so buggy
        self.populate()
        self.drawNodes(True) #updates
        #self.draw_edges(True) #updates

    # def draw_edges(self, update=False):
    #     print("draw_edges")
    #     prevNode = self.gridAry[0,0]
    #     if not update:
    #         for (r, c), n in np.ndenumerate(self.gridAry):
    #             self.create_line([n.center, prevNode.center], tags=[n.name+'line'])
    #             prevNode = n
    #     else:
    #         for (r, c), n in np.ndenumerate(self.gridAry):
    #             self.coords(n.name+'line', n.pos)

    def set_neighbors(self):
        '''puts the neighbors of each node'''
        grid_shape = self.grid_dimensions()
        for (r, c), n in np.ndenumerate(self.gridAry):
            node_left = self.gridAry[r, c-1] if c-1 > 0 else []
            node_right = self.gridAry[r,c+1] if c+1 < grid_shape[1] else []
            node_up = self.gridAry[r-1,c] if r-1 > 0 else []
            node_down = self.gridAry[r+1,c] if r+1 < grid_shape[0] else []
            n.neighbors = [node_left, node_right, node_up, node_down]
            print(n.neighbors)


    def grid_dimensions(self):
        return self.gridAry.shape #(x,y)

class Node():
    def __init__(self, name, color, position):
        '''each point on grid is a node
        position is the coordinates of the box of circle
        center if the real center coordinates'''
        self.name = name
        self.color = color
        self.passable = True
        self.pos = position #coordinates of the bounding box
        self.center = ((position[2]-position[0])/2)+position[0], ((position[3]-position[1]) /2)+position[1]
        self.neighbors = [] #list of neighboring nodes

    def invert_passable(self):
        self.passable = not self.passable
        self.color = 'grey'

    def r_passable(self):
        return self.passable

    def name_int(self):
        '''returns the name as a tuple of ints
        'x,y'
        (x,y)
        '''
        return int(self.name[0]), int(self.name[3])

if __name__ == '__main__':
    root = tk.Tk()
    gr = GridCanvas( root, 1, 2, width=500, height=500)
    gr.populate()
    gr.drawNodes()
    #gr.draw_edges()
    gr.set_neighbors()
    gr.pack(side="bottom", fill="both", expand=True)
    tk.mainloop()
# root = tk.Tk()
# gr = GridCanvas(root, 2, 3, width=500, height=500)
# gr.populate()
# gr.drawNodes()
# gr.pack(side="bottom", fill="both", expand=True)
# tk.mainloop()

# class Navigator():
#   self.options = ['djiskstra_navigate']
#   def __init__(start, end):
#     self.start_node = start
#     self.end_node = end
#
#   def r_options(self):
#     return self.options
#
#   def djikstra_navigate():
#     # implement djikstra navigation here
#
#     # represent grid as a tree
#     # if

  # #pulldown menu
  # ariable = StringVar(root)
  # navigation = Navigator.r_options()
  # ariable.set(navi) # default value
  #  = OptionMenu(root, variable, "one", "two", "three")
  # .pack()
  #
  # ainloop()gatoin

    # #pulldown menu
    # variable = StringVar(root)
    # navigation = Navigator.r_options()
    # variable.set(navigation[0]) # default value
    # w = apply(OptionMenu, (root, variable) + tuple(navigation))
    # w.pack()
    # mainloop()
