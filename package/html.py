from xml.etree import ElementTree
from typing import Sequence
from itertools import chain

from .search import Criteria


class Html:
    def __init__(self, path: str):
        self._root = ElementTree.parse(path)
        self._parents = dict((c, p) for p in self._root.iter() for c in p)

    def parent(self, element) -> ElementTree.Element:
        return self._parents.get(element)

    def elements(self, tag=None, **kwargs):
        def attributes_equal(element, attributes):
            for name in attributes:
                if element.get(name) != attributes[name]:
                    return False
            return True

        for x in self._root.iter(tag):
            if attributes_equal(x, kwargs):
                yield x

    def element(self, tag=None, **kwargs):
        for x in self.elements(tag, **kwargs):
            return x


class HtmlElementPattern:
    @staticmethod
    def of(html: Html, *, id: str):
        return HtmlElementPattern(html, html.element(id=id))

    def __init__(self, html: Html, inner: ElementTree.Element):
        self._html = html
        self._inner = inner

    @property
    def inner(self):
        return self._inner

    @property
    def path(self):
        def parts_of_path(x):
            if x is None:
                return

            parent = self._html.parent(x)
            index = list(parent).index(x) if parent is not None else 0
            index = f"[{index}]" if index > 0 else ""

            yield f"{x.tag}{index}"
            yield from parts_of_path(parent)

        parts = list(parts_of_path(self._inner))
        parts = reversed(parts)

        return " -> ".join(parts)

    def find_in(self, other: Html, *criterias: Sequence[Criteria]):
        groups = [x.elements(other, self._inner) for x in criterias]
        groups = list(chain(*groups))

        dictionary = {}
        for (x, score) in groups:
            if dictionary.get(x) is None:
                dictionary[x] = score
            else:
                dictionary[x] += score

        element = max(dictionary.keys(), key=lambda x: dictionary[x])

        return HtmlElementPattern(other, element)
