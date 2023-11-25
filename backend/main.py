from rdflib import Graph, URIRef, Literal
from graph_manager import GraphManager
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

gm = GraphManager()

gm.add("marco", "is", "character")
gm.add("marco", "is", "little")
gm.add("marco", "is", "boy")
gm.add("ancient rome", "is", "place")
gm.add("ancient rome", "is", "city")
gm.add("marco", "lives in", "ancient rome")
gm.add("pollo", "is", "character")
gm.add("pollo", "is", "dog")
gm.add("pollo", "is", "little")



response = gm.query("""    
SELECT ?subject ?predicate ?object
WHERE {
    ?subject ?predicate ?object .
    FILTER (STR(?predicate) = "edge")
}
""")

print(response.serialize().decode("utf-8"))

gm.save()

# Once upon a time, there was a curious little boy named Marco who lived in Ancient Rome. He had a loyal companion, his dog Pollo, who he loved dearly. One day, while exploring the bustling streets of Rome with Pollo by his side, Marco became distracted and lost track of where they were.
# As they wandered aimlessly through the city's labyrinthine alleyways, night began to fall and they realized that they had no idea how to find their way home. They saw many unfamiliar sights - grand temples dedicated to Roman gods, lively marketplaces filled with exotic wares from far-off lands, and even a gladiatorial arena where fierce battles once took place.
# Despite his fears, Marco remained determined not to give up hope. He knew that if he could just find someone who spoke Latin, the language of Ancient Rome, they might be able to help them navigate back home. But as they searched high and low for someone who fit this description, it seemed like everyone they encountered only spoke in strange tongues or were too busy with their own business.
# Just when all hope seemed lost, Marco spotted an old man sitting on a bench near one of the city's many fountains. He approached him cautiously and asked if he could speak Latin. To his surprise, the man nodded kindly and replied in the ancient language.
# Overjoyed at finally finding someone who could understand them, Marco explained their predicament to the old man. After hearing their story, the kind-hearted old soul decided to help them find their way back home using his extensive knowledge of the city's layout.
# As they set off on their journey, Marco and Pollo followed the old man through winding streets and across bustling plazas filled with colorful characters from all walks of life. Along the way, they passed many famous landmarks - the Colosseum where gladiators once fought to the death for entertainment; the Pantheon, a temple dedicated to all Roman gods; and even the Forum, the center of political life in Ancient Rome.
# After what seemed like hours of walking, they finally arrived back at Marco's home. His parents were overjoyed to see him safe and sound, having been frantic with worry since he went missing. They hugged their son tightly and thanked the old man profusely for his help in bringing them back together.
# From that day forward, Marco never forgot the kindness of the stranger who helped him find his way home during his time of need. And every time he looked into Pollo's big brown eyes, he remembered the adventure they shared and how close they came to losing each other forever in the winding streets of Ancient Rome.