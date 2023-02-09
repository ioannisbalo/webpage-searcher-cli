from webpage_searcher import Result
from rich.console import Console
from rich.table import Table

from src.app import Results
from src.output.output import Output


class PrintOutput(Output):
    def __init__(self) -> None:
        self._console = Console()
        self._table = Table(show_header=True, header_style="bold magenta")
        self._table.add_column("Webpage", style="green")
        self._table.add_column("Phrase", style="green")
        self._table.add_column("Url", style="green")
        self._table.add_column("Tag")
        self._table.add_column("Link")
        self._table.add_column("NoFollow")
        self._table.add_column("Xpath")
        self._table.add_column("Text")
        self._table.add_column("Context")

    def write(self, results: list[Results]) -> None:
        for webpage_results in results:
            self._write_webpage_results(webpage_results)
        self._console.print(self._table)

    def _write_webpage_results(self, webpage_results: Results) -> None:
        if webpage_results.phrase:
            self._write_item_results(webpage_results.phrase_results, webpage_results.webpage, webpage_results.phrase, None)
        if webpage_results.url:
            self._write_item_results(webpage_results.url_results, webpage_results.webpage, None, webpage_results.url)

    def _write_item_results(self, results: list[Result], webpage: str, phrase: str, url: str) -> None:
        for result in results:
            self._write_result(result, webpage, phrase, url)

    def _write_result(self, result: Result, webpage: str, phrase: str, url: str) -> None:
        self._table.add_row(
            self._format_output_string(webpage, True),
            self._format_output_string(phrase, True),
            self._format_output_string(url, True),
            result.tag,
            self._format_output_string(result.link.href, False) if result.link is not None else "-",
            str(result.link.nofollow) if result.link is not None else "-",
            self._format_output_string(result.xpath, False),
            self._format_output_string(result.string, True),
            self._format_output_string(result.context, True),
        )

    def _format_output_string(self, output: str, trim: bool) -> str:
        if not output:
            return "-"
        if trim:
            return output if len(output) < 20 else f"{output[:18]}..."
        return output
