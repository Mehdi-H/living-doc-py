from datetime import date
import pytest

from living_doc.living_glossary import (
    Concept,
    concepts_to_markdown_list,
    concepts_to_markdown_table,
)


@pytest.mark.unit
def test_present_one_concept_to_markdown_list():
    # Arrange
    concepts = {
        Concept(
            name="CatActivity",
            desc="The set of the main activities of a cat",
            origin=__file__,
        )
    }

    # Act
    glossary = concepts_to_markdown_list(concepts)

    # Assert
    assert (
        glossary
        == f"""# Glossary

![](https://img.shields.io/static/v1?label=Generated_on&message={date.today()}&color=blue)

- [CatActivity]({__file__}) : The set of the main activities of a cat
"""
    )


@pytest.mark.unit
def test_present_concepts_to_markdown_list():
    # Arrange
    concepts = {
        Concept(
            name="CatActivity",
            desc="The set of the main activities of a cat",
            origin=__file__,
        ),
        Concept(
            name="Sleeping",
            desc="The cat is sleeping with its two eyes closed",
            origin=__file__,
        ),
    }

    # Act
    glossary = concepts_to_markdown_list(concepts)

    # Assert
    assert (
        glossary
        == f"""# Glossary

![](https://img.shields.io/static/v1?label=Generated_on&message={date.today()}&color=blue)

- [CatActivity]({__file__}) : The set of the main activities of a cat
- [Sleeping]({__file__}) : The cat is sleeping with its two eyes closed
"""
    )


@pytest.mark.unit
def test_present_one_concept_to_markdown_table():
    # Arrange
    concepts = {
        Concept(
            name="CatActivity",
            desc="The set of the main activities of a cat",
            origin=__file__,
        )
    }

    # Act
    glossary = concepts_to_markdown_table(concepts)

    # Assert
    assert (
        glossary
        == f"""# Glossary

![](https://img.shields.io/static/v1?label=Generated_on&message={date.today()}&color=blue)

| Concept   | Description  |
|---|---|
| [CatActivity]({__file__}) | The set of the main activities of a cat |
"""
    )


@pytest.mark.unit
def test_present_concepts_to_markdown_table():
    # Arrange
    concepts = {
        Concept(
            name="CatActivity",
            desc="The set of the main activities of a cat",
            origin=__file__,
        ),
        Concept(
            name="Sleeping",
            desc="The cat is sleeping with its two eyes closed",
            origin=__file__,
        ),
    }

    # Act
    glossary = concepts_to_markdown_table(concepts)

    # Assert
    assert (
        glossary
        == f"""# Glossary

![](https://img.shields.io/static/v1?label=Generated_on&message={date.today()}&color=blue)

| Concept   | Description  |
|---|---|
| [CatActivity]({__file__}) | The set of the main activities of a cat |
| [Sleeping]({__file__}) | The cat is sleeping with its two eyes closed |
"""
    )
