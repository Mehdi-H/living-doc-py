import ast
from dataclasses import dataclass
from typing import Set

from living_doc.annotations import Glossary

from datetime import date


@dataclass(frozen=True)
class Concept:
    name: str
    desc: str
    origin: str


Concepts = Set[Concept]


def find_concepts_from(
    source_code: str,
    origin: str = __file__,
    glossary_decorator: str = Glossary.__name__,
) -> Concepts:
    concepts: Concepts = set()
    tree = ast.parse(source_code)
    tree_with_only_python_classes = filter(
        lambda n: isinstance(n, ast.ClassDef), ast.walk(tree)
    )
    for node in tree_with_only_python_classes:
        decorators = filter(lambda i: isinstance(i, ast.Name), node.decorator_list)
        for item in decorators:
            if item.id == glossary_decorator:
                concepts.add(Concept(node.name, ast.get_docstring(node), origin))
    return concepts


def concepts_to_markdown_list(concepts: Concepts) -> str:
    markdown_glossary = f"""# Glossary

![](https://img.shields.io/static/v1?label=Generated_on&message={date.today()}&color=blue)

"""
    for c in sorted(concepts, key=lambda concept: concept.name):
        markdown_glossary += f"- [{c.name}]({c.origin}) : {c.desc}\n"
    return markdown_glossary


def concepts_to_markdown_table(concepts: Concepts) -> str:
    markdown_glossary = f"""# Glossary

![](https://img.shields.io/static/v1?label=Generated_on&message={date.today()}&color=blue)

| Concept   | Description  |
|---|---|
"""
    for c in sorted(concepts, key=lambda concept: concept.name):
        markdown_glossary += f"| [{c.name}]({c.origin}) | {c.desc} |\n"
    return markdown_glossary
