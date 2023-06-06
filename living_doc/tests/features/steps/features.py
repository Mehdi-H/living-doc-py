from behave import given, when, then

from living_doc.glossary_strategy import Glossary, MarkdownListStrategy
from living_doc.living_glossary import find_concepts_from


@given("some business concepts have been annotated in the code")
def some_business_concepts_have_been_annontated(context):
    context.annotated_code = context.text


@when("living-doc is run on this code")
def living_doc_is_ran_on_this_code(context):
    concepts = find_concepts_from(context.annotated_code)
    md_list_glossary_exporter = Glossary(MarkdownListStrategy, concepts)
    context.glossary = md_list_glossary_exporter.to_glossary()


@then("a glossary with these concepts is generated")
def a_glossary_with_these_concepts_is_generated(context):
    assert context.text in context.glossary
