from src.output.print_output import PrintOutput
from src.csv_util import csv_input
from src.input import CliArguments, Input
from src.app import App


class Settings:
    def __init__(self, args: CliArguments):
        if args.input_file:
            inputs = csv_input(args.input_file)
        else:
            inputs = [Input({"webpage": args.webpage, "url": args.url, "phrase": args.phrase})]

        output = PrintOutput()
        self.app = App(inputs, args.url, args.phrase, output)

    def get_app(self) -> App:
        return self.app

