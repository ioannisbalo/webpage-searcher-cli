from dataclasses import dataclass
from typing import Optional

from webpage_searcher import UrlFinder, PhraseFinder

from src.input import Input
from src.http import get_html
from src.output.results import Results
from src.output.output import Output


class App:
    def __init__(
        self,
        inputs: list[Input],
        default_url: Optional[str],
        default_phrase: Optional[str],
        output: Output,
    ) -> None:
        self._inputs = inputs
        self._default_url = default_url
        self._default_phrase = default_phrase
        self._output = output

    def run(self) -> None:
        total_results = []
        for input in self._inputs:
            total_results.append(self._process(input))
        self._output.write(total_results)

    def _process(self, input: Input) -> Results:
        url = input.url if input.url else self._default_url
        phrase = input.phrase if input.phrase else self._default_phrase
        if not url and not phrase:
            raise ValueError(f"No url or phrase provided for webpage {input.webpage}, skipping")

        html = get_html(input.webpage)
        url_results = []
        if url:
            url_finder = UrlFinder(html)
            url_results = url_finder.find(url)
        phrase_results = []
        if phrase:
            phrase_finder = PhraseFinder(html)
            phrase_results = phrase_finder.find(phrase)
        return Results(webpage=input.webpage, url=url, phrase=phrase, url_results=url_results, phrase_results=phrase_results)
