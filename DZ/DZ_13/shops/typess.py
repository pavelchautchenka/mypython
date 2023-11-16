from dataclasses import dataclass


@dataclass
class Components:
    id: int
    name: str
    price: float


@dataclass
class Mothercard(Components):
    mem: int
    cls: str


@dataclass
class Videocard(Components):
    memo: int
    cls: str


@dataclass
class Article:
    id: int
    name: str
    price: float

@dataclass
class Book(Article):
    title: str

@dataclass
class Magazine(Article):
    title: str


@dataclass
class Product:
    id: int
    name: str
    price: float


@dataclass
class Pizza(Product):
    diameter: int
    spicy: str


@dataclass
class Coffee(Product):
    size: str

@dataclass
class Furniture(Product):
    type: str

@dataclass
class Table(Furniture):
    forme: str


@dataclass
class Chair(Furniture):
    material: str


@dataclass
class Locker(Furniture):
    size: str

@dataclass
class L:
    size: str