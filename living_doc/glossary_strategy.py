from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Union

from living_doc.living_glossary import (
    Concepts,
    concepts_to_markdown_list,
    concepts_to_markdown_table,
)


@dataclass
class ExportStrategy(ABC):
    @abstractmethod
    def to_glossary(cls, concepts: Concepts) -> Union[str, None]:
        pass

    @abstractmethod
    def write_glossary_to(cls, file: str, concepts: Concepts) -> None:
        pass


@dataclass
class Glossary:
    strategy: ExportStrategy
    concepts: Concepts

    def to_glossary(cls) -> Union[str, None]:
        return cls.strategy.to_glossary(cls.concepts)

    def write_glossary_to(cls, file) -> None:
        cls.strategy.write_glossary_to(file, cls.concepts)


@dataclass
class MarkdownListStrategy(ExportStrategy):
    @classmethod
    def to_glossary(cls, concepts: Concepts) -> str:
        return concepts_to_markdown_list(concepts)

    @classmethod
    def write_glossary_to(cls, file, concepts) -> None:
        with open(file, "w") as glossary:
            glossary.write(cls.to_glossary(concepts))


@dataclass
class MarkdownTableStrategy(ExportStrategy):
    @classmethod
    def to_glossary(cls, concepts: Concepts) -> str:
        return concepts_to_markdown_table(concepts)

    @classmethod
    def write_glossary_to(cls, file, concepts) -> None:
        with open(file, "w") as glossary:
            glossary.write(cls.to_glossary(concepts))
