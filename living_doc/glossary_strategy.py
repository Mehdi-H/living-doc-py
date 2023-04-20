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
    def to_glossary(self, concepts: Concepts) -> Union[str, None]:
        pass

    @abstractmethod
    def write_glossary_to(self, file: str) -> None:
        pass


@dataclass
class Glossary:
    strategy: ExportStrategy
    concepts: Concepts

    def to_glossary(self) -> Union[str, None]:
        return self.strategy.to_glossary(self.concepts)

    def write_glossary_to(self, file) -> None:
        self.strategy.write_glossary_to(file, self.concepts)


@dataclass
class MarkdownListStrategy(ExportStrategy):
    @classmethod
    def to_glossary(self, concepts: Concepts) -> str:
        return concepts_to_markdown_list(concepts)

    @classmethod
    def write_glossary_to(self, file, concepts) -> None:
        with open(file, "w") as glossary:
            glossary.write(self.to_glossary(concepts))


@dataclass
class MarkdownTableStrategy(ExportStrategy):
    @classmethod
    def to_glossary(self, concepts: Concepts) -> str:
        return concepts_to_markdown_table(concepts)

    @classmethod
    def write_glossary_to(self, file, concepts) -> None:
        with open(file, "w") as glossary:
            glossary.write(self.to_glossary(concepts))
