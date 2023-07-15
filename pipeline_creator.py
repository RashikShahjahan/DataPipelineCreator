import json
import sys
import networkx as nx
from collections import defaultdict
import ray
import subprocess

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def create_directed_graph(prerequisite_map):
    graph = nx.DiGraph()
    host_map = {}
    for step, details in prerequisite_map.items():
        graph.add_node(step)
        host_map[step] = details["host"]
        for prerequisite in details["prerequisites"]:
            graph.add_edge(prerequisite, step)
    return graph, host_map


def get_levelwise_ordering(graph):
    try:
        return list(nx.topological_sort(graph))
    except nx.NetworkXUnfeasible:
        print("The prerequisite map contains a cycle, so no valid ordering exists.")
        return []

@ray.remote
class ScriptExecutor:
    def execute_script(self, script_path, input_file, output_file, host):
        process = subprocess.run(
            ["python3", "scripts/"+script_path, input_file, output_file],
            text=True,
            capture_output=True,
        )
        if process.returncode != 0:
            print(f"Script {script_path} failed with exit code {process.returncode}.")
            print(process.stderr)
        return output_file

def execute_level(scripts_with_io):
    executors = [ScriptExecutor.remote() for _ in scripts_with_io]
    results = [executor.execute_script.remote(*args) for executor, args in zip(executors, scripts_with_io)]
    return ray.get(results)


def main():
    ray.init(address='auto')
    file_path = 'pipelines/'+sys.argv[1]  # replace with your file path
    input_csv = 'inputs/'+sys.argv[2] # replace with your input CSV file path
    prerequisite_map = load_json_file(file_path)
    graph, host_map = create_directed_graph(prerequisite_map)
    ordering = get_levelwise_ordering(graph)
    level_dict = defaultdict(list)
    for node in graph:
        level = len(nx.ancestors(graph, node))
        level_dict[level].append(node + ".py")

    input_data = input_csv
    for level in sorted(level_dict.keys()):
        output_files = []
        for script in level_dict[level]:
            output_file = f'outputs/{script[:-3]}_output_{level}.csv'
            output_files.append(output_file)
        input_data = execute_level([(script, input_data, output_file, host_map[script[:-3]]) for script, output_file in zip(level_dict[level], output_files)])
        input_data = input_data[-1] if input_data else None


if __name__ == "__main__":
    main()
