from rdflib import Graph, URIRef, Literal
from graph_manager import GraphManager

# Create a new graph
gm = GraphManager()

# Add triples to the graph
gm.add("foo", "edge", "bar")
gm.add("bar", "edge", "baz")
gm.add("baz", "edge", "foo")

response = gm.query("""    
SELECT ?subject ?predicate ?object
WHERE {
    ?subject ?predicate ?object .
    FILTER (STR(?predicate) = "edge")
}
""")

print(response.serialize().decode("utf-8"))

# Serialize the graph to a string in Turtle format
# response.serialize(destination="graph.ttl")

gm.save()

# g.serialize(destination="graph.ttl", format="turtle")