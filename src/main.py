# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

TAGS = [
    ["{", "}"],
    ["[", "]"],
    ["(", ")"]
]


def closing(char: str, tag: List[str], tag_stack: List[str]) -> bool:
    return char == tag[1] and len(tag_stack) > 0 and tag[0] in tag_stack


def opening(char: str, tag: List[str]) -> bool:
    return char == tag[0]


def process_tag(char, tag, tag_stack: List[str]):
    if opening(char, tag):
        tag_stack.append(char)
    if closing(char, tag, tag_stack):
        tag_stack.remove(tag[0])


def check_nested(s: str) -> int:
    tag_stack = []
    for i in range(0, len(s)):
        [process_tag(s[i], tag, tag_stack) for tag in TAGS]
    return 1 if len(tag_stack) == 0 else 0