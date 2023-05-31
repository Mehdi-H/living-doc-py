Feature: showing off living-doc-py

  Scenario: run a simple test
    Given some business concepts have been annotated in the code
      '''
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
      '''
    When living-doc is run on this code
    Then a glossary with these concepts is generated
      """
      - [CatActivity](/Users/mehdi.houacine/Documents/r-et-d/living-doc-py/living_doc/living_glossary.py) : The set of the main activities of a cat
      - [Chasing](/Users/mehdi.houacine/Documents/r-et-d/living-doc-py/living_doc/living_glossary.py) : The cat is actively chasing, eyes wide open
      - [Eating](/Users/mehdi.houacine/Documents/r-et-d/living-doc-py/living_doc/living_glossary.py) : The cat is eating, or very close to the dish
      - [Event](/Users/mehdi.houacine/Documents/r-et-d/living-doc-py/living_doc/living_glossary.py) : Anything  that can happen that matters to the cat
      - [Sleeping](/Users/mehdi.houacine/Documents/r-et-d/living-doc-py/living_doc/living_glossary.py) : The cat is sleeping with its two eyes closed
      """