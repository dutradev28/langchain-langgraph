from typing import Annotated, TypedDict, Literal
from langgraph.graph import StateGraph, END, START
from rich import print
from dataclasses import dataclass
import operator


#1 - Definir o meu estado
@dataclass
class State:
    nodes: Annotated[list[str], operator.add]
    current_number: int = 0
    
#2 - Definir os estados

def node_a(state: State) -> State:    
    output_state: State = State(nodes=["A"], current_number=state.current_number)
    print("> node_a", f"{state=}", f"{output_state=}")
    
    return output_state

def node_b(state: State) -> State:
    output_state: State = State(nodes=["B"], current_number=state.current_number)
    print("> node_b", f"{state=}", f"{output_state=}")
    
    return output_state

def node_c(state: State) -> State:
    output_state: State = State(nodes=["C"], current_number=state.current_number)
    print("> node_c", f"{state=}", f"{output_state=}")
    
    return output_state

def the_conditional(state: State) -> Literal["B", "C"]:
    if state.current_number > 50:
        return "C"
    return "B"

builder = StateGraph(State)

builder.add_node("A", node_a)
builder.add_node("B", node_b)
builder.add_node("C", node_c)

#3 - Conectar as edges

builder.add_edge(START, "A")
builder.add_conditional_edges("A", the_conditional, {"B", "C"})
builder.add_edge("B", END)
builder.add_edge("C", END)

#4 - Compilar o grafo

graph =  builder.compile()

#5 - Result do graph
print()
response = graph.invoke(State(nodes=[]))
print(f"{response=}")
print()

print()
response = graph.invoke(State(nodes=[], current_number=51))
print(f"{response=}")
print()



    
