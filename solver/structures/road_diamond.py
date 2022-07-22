from base import Diamond_cell


class Road_Diamond(Diamond_cell):
    """
    Class for patch of road on diamond cell in the game.
    """

    def __init__(self, g, node_labels) -> None:
        super().__init__(g, node_labels)

    def __call__(self, active_dir) -> None:
        n_active = 0
        for direction, active in active_dir.items():
            if not active:
                self.del_nodes.append(direction)
            else:
                n_active += 1
        prev=None
        for direction, active in active_dir.items():
            if (active and prev==None):
                first_active=direction
                prev = direction
            if (active and prev!=None):
                self.add_edges(prev, direction)
                prev = direction
        self.add_edges(prev, first_active)
        return super().__call__(active_dir)
