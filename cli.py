import os
from typing import List


class Cli:

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    @classmethod
    def get_multi_line_input(cls, message: str):
        cls.clear()
        print(f'{message}\n to finish type single "." in last line')

        multi_line_input = []
        while True:
            line = input()
            if line == ".":
                break
            multi_line_input.append(line)

        return '\n'.join(multi_line_input)

    @classmethod
    def get_line(cls, message: str):
        cls.clear()
        return input(message)

    @classmethod
    def print_msg(cls, message: str):
        cls.clear()
        print(message)
        input('\npress Enter to continue')

    @classmethod
    def menu_choice(cls, choices: List[str]):
        cls.clear()

        for i, choice in enumerate(choices, start=1):
            print(f'{i} - {choice}')

        valid_answer = None
        while not valid_answer:
            answer = input('>> ')
            try:
                answer = int(answer)
            except ValueError:
                print('select correct answer')
                continue
            valid_answer = True

        return choices[answer - 1]
