from typing import List, Set, Dict, Tuple, Callable, Optional, TypeVar, Sequence, Any, TypedDict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Generics')

numbers: List[int] = [1, 2, 3, 4]
names: Set[str] = {"sameer", "mayuri"}
nameToEmails: Dict[str, List[str]] = {"sameer": ["sam@gmail.com"]}

nameOptional: Optional[str] = ""
T = TypeVar("T")


def get_element( elements: List[T], index: int ):
    return elements[index]


element = get_element([1, 2, 3, 4], 2)
print(element)

element = get_element(["Java", "Javascript", "Kotlin"], 2)
print(element)

numbers: list = [1, 2, 3, 4]
assortedBasket: tuple = (1, "name")
nameToEmails: dict = {"sameer": ["sam@gmail.com"]}

marks: Sequence[int] = [90, 85, 88]


