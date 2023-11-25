from rdflib import Graph, URIRef, Literal
from graph_manager import GraphManager

gm = GraphManager()

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

gm.save()