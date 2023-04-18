import ast
from dataclasses import dataclass
from typing import Set

from living_doc.annotations import Glossary


@dataclass(frozen=True)
class Concept:
    name: str
    desc: str
    origin: str

Concepts = Set[Concept]

def find_concepts_from(source_code: str, origin: str, glossary_decorator: str = Glossary.__name__) -> Concepts:
    concepts : Concepts = set()
    tree=ast.parse(source_code)
    tree_with_only_python_classes = filter(lambda n : isinstance(n, ast.ClassDef), ast.walk(tree))
    for node in tree_with_only_python_classes:
        decorators = filter(lambda i : isinstance(i, ast.Name), node.decorator_list)
        for item in decorators:
            if item.id == glossary_decorator:
                concepts.add(Concept(node.name, ast.get_docstring(node), origin))
    return concepts
