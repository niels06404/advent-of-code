"""
Advent of Code 2023 - Utils Module

This module provides utility functions for handling input files and 
running and asserting solutions for Advent of Code 2023.

Author: Niels Schröder
Date: 2023/11/29

Functions:
    - read_file(filepath: str) -> List[str]: Reads the content of a 
        file and returns each line as a string in a list.
    - read_puzzle_input(day: int) -> List[str]: Reads the puzzle input
        file for the given Advent of Code day.
    - run_and_assert(day: int, solution_function: callable, 
        expected_answer: any) -> None: Runs the provided solution 
        function on the example input and asserts the result.
"""
import os


def read_file(filepath: str) -> list[str]:
    """Reads the content of a file and returns each line as a string in
      a list.

    Args:
        filepath (str): The path to the file to be read.

    Returns:
        List[str]: A list containing each line of the file as a string.

    Raises:
        FileNotFoundError: If the file is not found.
    """
    try:
        with open(filepath, mode="r", encoding="utf-8") as file:
            return [line.rstrip() for line in file]
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {filepath}") from e


def read_puzzle_input(day: int) -> list[str]:
    """Reads the puzzle input file for the given Advent of Code day.

    Args:
        day (int): The day for which to read the puzzle input.

    Returns:
        List[str]: A list containing each line of the puzzle input file
          as a string.

    Raises:
        FileNotFoundError: If the puzzle input file for the given day
          is not found.
    """
    input_filename = f"day_{day}.txt"
    input_filepath = os.path.join("..", "input", input_filename)
    return read_file(input_filepath)


def run_and_assert(
    day: int | str, solution_function: callable, expected_answer: any
) -> None:
    """Runs the provided solution function on the example input and
      asserts the result.

    Args:
        day (int): The day for which to run the example.
        solution_function (callable): The function to be tested.
        expected_answer (Any): The expected answer for the example.

    Raises:
        FileNotFoundError: If the example input file for the given day
          is not found.
        AssertionError: If the result of the function does not match
          the expected answer.
    """
    example_filename = f"day_{day}_example.txt"
    example_filepath = os.path.join("..", "input", example_filename)
    example_input = read_file(example_filepath)

    result = solution_function(example_input)
    assert (
        result == expected_answer
    ), f"Expected: {expected_answer}, Got: {result}"
