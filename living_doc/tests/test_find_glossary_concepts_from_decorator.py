import pytest

from living_doc.living_glossary import Concept, find_concepts_from


@pytest.mark.unit
def test_find_glossary_concepts_from_source_code():
    # Arrange
    source_code = '''
@Glossary
class CatActivity:
    """The set of the main activities of a cat"""
    pass

@Glossary
class Sleeping(CatActivity):
    """The cat is sleeping with its two eyes closed"""
    pass
'''

    # Act
    concepts = find_concepts_from(source_code, origin=__name__)

    # Assert
    assert concepts == {
        Concept(
            name="CatActivity",
            desc="The set of the main activities of a cat",
            origin=__name__,
        ),
        Concept(
            name="Sleeping",
            desc="The cat is sleeping with its two eyes closed",
            origin=__name__,
        ),
    }


@pytest.mark.unit
def test_concepts_not_decorated_with_glossary_are_ignored():
    # Arrange
    source_code = '''
@Glossary
class CatActivity:
    """The set of the main activities of a cat"""
    pass

@dataclass
class Sleeping(CatActivity):
    """The cat is sleeping with its two eyes closed"""
    pass
'''

    # Act
    concepts = find_concepts_from(source_code, origin=__name__)

    # Assert
    assert concepts == {
        Concept(
            name="CatActivity",
            desc="The set of the main activities of a cat",
            origin=__name__,
        ),
    }


@pytest.mark.unit
def test_find_glossary_concepts_even_if_class_has_multiple_decorators_applied_in_any_order():
    # Arrange
    source_code = '''
@Glossary
class CatActivity:
    """The set of the main activities of a cat"""
    pass

@Glossary
@dataclass
class Sleeping(CatActivity):
    """The cat is sleeping with its two eyes closed"""
    pass

@dataclass
@Glossary
class Eating(CatActivity):
    """The cat is eating, or very close to the dish"""
    pass
'''

    # Act
    concepts = find_concepts_from(source_code, origin=__name__)

    # Assert
    assert concepts == {
        Concept(
            name="CatActivity",
            desc="The set of the main activities of a cat",
            origin=__name__,
        ),
        Concept(
            name="Sleeping",
            desc="The cat is sleeping with its two eyes closed",
            origin=__name__,
        ),
        Concept(
            name="Eating",
            desc="The cat is eating, or very close to the dish",
            origin=__name__,
        ),
    }
