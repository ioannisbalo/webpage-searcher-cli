from dataclasses import dataclass

from webpage_searcher import Result


@dataclass
class Results:
    webpage: str
    url: str
    phrase: str
    url_results: list[Result]
    phrase_results: list[Result]
