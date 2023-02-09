from typing import Optional


class Input:
    webpage: str
    url: Optional[str]
    phrase: Optional[str]

    def __init__(self, input_dict: dict[str, str]):
        self.webpage = input_dict["webpage"]
        self.url = input_dict.get("url")
        self.phrase = input_dict.get("phrase")


class CliArguments:
    webpage: Optional[str]
    input_file: Optional[str]
    phrase: Optional[str]
    url: Optional[str]

    def __init__(
        self,
        webpage: Optional[str],
        input_file: Optional[str],
        phrase: Optional[str],
        url: Optional[str],
    ) -> None:
        if input_file and webpage:
            print("Both input csv file and webpage url provided, webpage url will be ignored")
        if not input_file and not webpage:
            raise ValueError("Please provide either a webpage url or an input csv file")
        if not input_file and not url and not phrase:
            raise ValueError("Please provide either a url or a phrase to be searched for")
        self.webpage = webpage
        self.input_file = input_file
        self.phrase = phrase
        self.url = url