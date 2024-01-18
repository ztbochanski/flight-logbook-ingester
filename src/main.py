import typer

from pdf_to_csv import convert_pdfs

cli = typer.Typer()


@cli.command()
def about():
    """Flight Logbook CLI
    """
    typer.echo("Flight Logbook Ingester CLI")


@cli.command()
def convert(directory='data'):
    """Ingests data from PDFs and outputs CSVs
    """
    typer.echo("Reading scanned docs...")
    convert_pdfs(directory=directory)
    typer.echo("✅ Done")


if __name__ == "__main__":
    cli()
