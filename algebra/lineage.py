import yaml
import networkx as nx
import matplotlib.pyplot as plt

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def create_lineage_graph(data):
    graph = nx.DiGraph()
    for transformation in data['transformations']:
        graph.add_node(transformation['target'])
        sources = transformation['source'].split(",")
        for source in sources:
            graph.add_edge(source, transformation['target'])
    return graph

def visualize_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='skyblue',
            node_size=2000, font_size=10, font_weight='bold',
            arrowsize=20)
    plt.title("Table Lineage Graph")
    plt.show()

if __name__ == '__main__':
    yaml_file = 'C:\\Users\\mravi\\Personal\\work\\AI_Journey\\transformations.yaml'
    yaml_data = load_yaml(yaml_file)
    lineage_graph = create_lineage_graph(yaml_data)
    visualize_graph(lineage_graph)
