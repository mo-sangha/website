from typing import Generic, TypeVar
from rdflib import Graph, URIRef, Literal

AdditionalData = TypeVar("AdditionalData")

class GraphManager(Generic[AdditionalData]):
    g = Graph()

    def add(self, subject: str, predicate: str, object: str, additional_data: AdditionalData = None):
        self.g.add((Literal(subject), Literal(predicate), Literal(object)))
    
    def query(self, query: str):
        return self.g.query(query)

    def save(self):
        self.g.serialize(destination="graph.ttl", format="turtle")