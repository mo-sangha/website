from rdflib import Graph, URIRef, Literal

# Create a new graph
g = Graph()

# Define the nodes and predicate
foo = Literal("foo")
bar = Literal("bar")
baz = Literal("baz")
edge = Literal("edge")

# Add triples to the graph
g.add((foo, edge, bar)) # foo -> bar
g.add((bar, edge, baz)) # bar -> baz
g.add((baz, edge, foo)) # baz -> foo

q = """
SELECT ?x
WHERE {
    ?x <edge> ?y
}
"""

# Serialize the graph to a string in Turtle format
print(g.serialize(format="turtle"))

g.serialize(destination="graph.ttl", format="turtle")