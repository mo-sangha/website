from rdflib import Graph, URIRef, Literal

class GraphManager():
    g = Graph()

    def add(self, subject: str, predicate: str, object: str):
        self.g.add((Literal(subject), Literal(predicate), Literal(object)))
    
    def query(self, query: str):
        return self.g.query(query)

    def save(self):
        self.g.serialize(destination="graph.ttl", format="turtle")