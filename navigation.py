#may have to change
#probably won't need trees but here just in case

def tree(label,branches):
    for b in branches: #branches must be trees
        assert is_tree(branch)
        return [label] +list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
        return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

class Navigation:

#start
#start
    def __init__(self, start, end, grid): #both start and end should be pairs, grid is grid object
        self.start = start #should stay static
        self.end = end
        self.grid = grid
        self.visited_nodes = [] #keeps track if node has been tracked yet, redundancy issues: since the path to each nearby node is a constant, if we have already visited a node, it is redundant to visit it again.
        self.paths = []
    #ARCHAIC
    #def check_node(self, position): #returns boolean(node valid to travel to) \\returns true if node is valid, take in position as a tuple
    #    x_grid, y_grid = self.grid.grid_dimensions()
    #    x_node, y_node = position #gets position of node
    #    if x_node >= x_grid or y_node >= y_grid or x_node < 0 or y_node < 0 or not node.r_passable(): #check if node is out of bounds
    #        return False
    #    return True
    #ARCHAIC
    # def nearby_nodes(self, current_node): #returns nearby valid nodes ARCHAIC
    #     x, y = current_node.name_int() #gets position of node
    #     directions = [(x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1)] #starts from North and goes clockwise
    #     nodes = [position for position in directions if self.check_node(position) or not position in self.visited_nodes] #removes the nearby node values that are invalid and previously visited nodes
    #     return nodes
    def check_neighbors(self, node):
        return node.r_passable()

    def treeify(self, node): #is node, not position
        self.visited_nodes.append(node)
        # if node == self.end:
        #     return [self.end]
        return tree(node,[self.treeify(node) for node in node.neighbors if node.r_passable() or not node in self.visited_nodes]) #nearby_nodes doesn't take position, it takes nodes

    def shortest_branch(self, t):
        if is_leaf(t):
            return [label(t)]
        else:
            for b in branches(t): #need length of branches of t somewhere in here
                self.paths.append(shortest_branches(b))
            return [label(t)] + min(paths, key = lambda x: len(x))

                #for b in branches(t): #need length of branches of t somewhere in here
 #               paths += shortest_branch(b)
  #          return min(paths, key = lambda x: len(paths[x]))


    #navigate from start to finish using dij method
    def dij(self):
        paths = self.treeify(self.start)
        most_efficient_path = shortest_branch(paths)
        print('Finished! Took {0} steps.'.format(len(most_efficient_path)))
        return most_efficient_path
