from dataclasses import astuple
from datetime import date
import click
import xlsxwriter
from living_doc.glossary_strategy import (
    MarkdownListStrategy,
    Glossary,
    MarkdownTableStrategy,
)

from living_doc.living_glossary import (
    concepts_to_markdown_list,
    concepts_to_markdown_table,
    find_concepts_from,
)


@click.group()
def cli():
    pass


@cli.command(name="from-module")
@click.argument("module", type=click.File("r"))
def from_module(module):
    source_code = module.read()
    concepts = find_concepts_from(source_code)
    glossary_as_markdown_list = concepts_to_markdown_list(concepts)
    click.echo("Writing the following into DEMO-GLOSSARY-AS-LIST.md :")
    click.echo(glossary_as_markdown_list)


@cli.command()
def demo():
    source_code = '''
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
    concepts = find_concepts_from(source_code)

    md_list_glossary_exporter = Glossary(MarkdownListStrategy, concepts)
    glossary_as_markdown_list = md_list_glossary_exporter.to_glossary()
    click.echo("Writing the following into DEMO-GLOSSARY-AS-LIST.md :")
    click.echo(glossary_as_markdown_list)
    md_list_glossary_exporter.write_glossary_to("DEMO-GLOSSARY-AS-LIST.md")

    md_table_glossary_exporter = Glossary(MarkdownTableStrategy, concepts)

    glossary_as_markdown_table = md_table_glossary_exporter.to_glossary()
    click.echo("Writing the following into DEMO-GLOSSARY-AS-TABLE.md :")
    click.echo(glossary_as_markdown_table)
    md_table_glossary_exporter.write_glossary_to("DEMO-GLOSSARY-AS-TABLE.md")

    workbook = xlsxwriter.Workbook("DEMO-GLOSSARY.xlsx")
    worksheet = workbook.add_worksheet()
    row, col = 0, 0
    worksheet.write(row, col, "Glossary")
    worksheet.write(row +1, col, f"Generated on {date.today()}")
    
    row, col = 3, 0
    for name, desc, _ in (astuple(concept) for concept in concepts):
        worksheet.write(row, col, name)
        worksheet.write(row, col + 1, desc)
        row += 1
    workbook.close()


if __name__ == "__main__":
    cli()
