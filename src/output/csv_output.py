import csv
from webpage_searcher import Result

from src.app import Results
from src.output.output import Output


class CsvOutput(Output):
    def __init__(self, verbose: bool, file: str) -> None:
        self._verbose = verbose
        self._file = file

    def write(self, results: list[Results]) -> None:
        with open(self._file, "w", encoding='UTF8') as f:
            self._writer = csv.writer(f)
            if self._verbose:
                self._writer.writerow(["Webpage", "Phrase", "Url", "Tag", "Link", "NoFollow", "Xpath", "Text", "Context"])
            else:
                self._writer.writerow(["Webpage", "Phrase", "Url", "Exists"])
            for webpage_results in results:
                self._write_webpage_results(webpage_results)

    def _write_webpage_results(self, webpage_results: Results) -> None:
        if webpage_results.phrase:
            self._write_item_results(webpage_results.phrase_results, webpage_results.webpage, webpage_results.phrase, None)
        if webpage_results.url:
            self._write_item_results(webpage_results.url_results, webpage_results.webpage, None, webpage_results.url)

    def _write_item_results(self, results: list[Result], webpage: str, phrase: str, url: str) -> None:
        if self._verbose:
            for result in results:
                self._write_result(result, webpage, phrase, url)
        else:
            self._writer.writerow([webpage, phrase, url, str(len(results) > 0)])

    def _write_result(self, result: Result, webpage: str, phrase: str, url: str) -> None:
        self._writer.writerow([
            webpage,
            phrase,
            url,
            result.tag,
            result.link.href if result.link is not None else "",
            str(result.link.nofollow) if result.link is not None else "",
            result.xpath,
            result.string,
            result.context,
        ])
