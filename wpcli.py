import argparse

from src.input import CliArguments
from src.csv_util import csv_input
from src.app import App
from src.settings import Settings


def main() -> None:
    parser = argparse.ArgumentParser(description="A command line tool that finds a url or a phrase in a website's html")

    parser.add_argument("-w", "--webpage", type=str, help="Url of the website to be searched")
    parser.add_argument("-u", "--url", type=str, help="Default url to be searched for in the website's links")
    parser.add_argument("-p", "--phrase", type=str, help="Default phrase to be searched for in the website's text")
    parser.add_argument("-i", "--input-file", type=str, help="Path to .csv file that contains webpages, urls and phrases")
    parser.add_argument("-o", "--output-file", type=str, help="Path to new .csv file to write the results of the search in")
    parser.add_argument("-v", "--verbose", action="store_true", help="Include the full results in the output")

    args = parser.parse_args()

    cli_args = CliArguments(args.webpage, args.phrase, args.url, args.input_file, args.output_file, args.verbose)
    settings = Settings(cli_args)
    app = settings.get_app()
    app.run()

if __name__ == "__main__":
    main()