from road_diamond import Road_Diamond
class Roundabout():
    """
    Class for Roundabouts in the game.
    """

    def __init__(self, g, node_labels_d1, node_labels_d2, node_labels_d3, node_labels_d4) -> None:
        self.d1=Road_Diamond(g, node_labels_d1)
        self.d2=Road_Diamond(g, node_labels_d2)     
        self.d3=Road_Diamond(g, node_labels_d3)
        self.d4=Road_Diamond(g, node_labels_d4)

    def __call__(self, active_dir_d1, active_dir_d2, active_dir_d3, active_dir_d4) -> None:
        self.d1(active_dir_d1)
        self.d2(active_dir_d2)
        self.d3(active_dir_d3)
        self.d4(active_dir_d4)