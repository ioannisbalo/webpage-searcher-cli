import csv
from webpage_searcher import Output

from src.input import Input


def csv_input(file: str) -> list[Input]:
    result = {}
    with open(file) as f:
        field_names = ["webpage", "url", "phrase"]
        reader = csv.DictReader(f, delimiter=",", fieldnames=field_names)
        result = [Input(line) for line in reader if line.get("webpage")]
    return result

# def csv_output(results: )

