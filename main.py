import abc
import argparse
from abc import abstractmethod

INPUT_TXT = """"""


class Solution(abc.ABC):
    @classmethod
    @abstractmethod
    def compute(cls, input_str: str) -> int:
        pass

    @classmethod
    @abstractmethod
    def run(cls, input_txt=INPUT_TXT) -> int:
        parser = argparse.ArgumentParser()
        parser.add_argument("input_file", nargs="?", default=input_txt)
        args = parser.parse_args()

        with open(args.input_file) as f:
            print(cls.compute(f.read()))

        return 0
