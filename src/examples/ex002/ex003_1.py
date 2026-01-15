from typing import Annotated, TypedDict
from langgraph.graph import StateGraph
from rich import print
import operator

# def reducer(a: list[str], b: list[str]) -> list[str]:
#     return a + b

#1 - Definir o meu estado
class State(TypedDict):
    nodes: Annotated[list[str], operator.add]
    
#2 - Definir os estados

def node_a(state: State) -> State:    
    output_state: State = {'nodes': ["A"]}
    print("> node_a", f"{state=}", f"{output_state=}")
    
    return output_state

def node_b(state: State) -> State:
    output_state: State = {'nodes': ["B"]}
    print("> node_b", f"{state=}", f"{output_state=}")
    
    return output_state

builder = StateGraph(State)

builder.add_node("A", node_a)
builder.add_node("B", node_b)

#3 - Conectar as edges

builder.add_edge("__start__", "A")
builder.add_edge("A", "B")
builder.add_edge("B", "__end__")

#4 - Compilar o grafo

graph =  builder.compile()

response = graph.invoke({"nodes": []})

#5 - Result do graph
print()
print(f"{response=}")
print()



    
