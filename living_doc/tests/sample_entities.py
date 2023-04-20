def Glossary(func):
    """To decorate a class that models a business concept. Its docstring will be used to feed a glossary file."""
    return func


@Glossary
class CatActivity:
    """The set of the main activities of a cat"""

    pass


@Glossary
class Sleeping(CatActivity):
    """The cat is sleeping with its two eyes closed"""

    pass


@Glossary
class Eating(CatActivity):
    """The cat is eating, or very close to the dish"""

    pass


@Glossary
class Chasing(CatActivity):
    """The cat is actively chasing, eyes wide open"""

    pass


@Glossary
class Event:
    """Anything  that can happen that matters to the cat"""

    pass
