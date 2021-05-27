#!/usr/bin/env python3

from adt import adt as sealed
from dataclasses import dataclass
from typing import Tuple


@sealed
class Sealed1:
    EMPTY: None
    INTEGER: int
    STRING_PAIR: Tuple[str, str]


x1 = Sealed1.INTEGER(5)
print(x1.integer())
x2 = Sealed1.EMPTY()
print(x2.empty())
x3 = Sealed1.STRING_PAIR("foo", "bar")
print(x3.string_pair())


@dataclass
class Leaf:
    data: int


@dataclass
class Node:
    left: "Tree"
    right: "Tree"


@sealed
class Tree:
    EMPTY: None
    LEAF: Leaf
    NODE: Node


t1 = Tree.EMPTY()
t2 = Tree.LEAF(3)
t3 = Tree.NODE((Tree.LEAF(3), Tree.LEAF(4)))
print(t1, t2, t3)
