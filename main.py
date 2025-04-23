from argparse import Namespace
import sys

class Runner:
    
    def __init__(self, os:str, os_ver:str) -> None:
        self.os = os
        self.os_ver = os_ver
    
    
    def run() -> None:
        pass


def main(args: Namespace) -> None:
    runner: Runner = Runner()
    pass


if __name__ == "__main__":
     main(sys.argv[1::])