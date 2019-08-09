from abc import ABCMeta, abstractmethod


def common_substring(x, y):
    # Naive implementation of LCS.
    def split(text, at):
        return text[:at], text[at:]

    lcs = ""

    for i in range(len(x)):
        start, end = split(x, at=i)
        if start in y:
            lcs = start if len(start) > len(lcs) else lcs
        elif end in y:
            lcs = end if len(end) > len(lcs) else lcs

    return lcs


def score(source, target):
    length = len(common_substring(source, target))
    return length / len(source)


def scored(html, source, *, by):
    value = source.get(by)
    elements = html.elements(**{by: value})

    return ((x, score(value, x.get(by))) for x in elements)


class Criteria(metaclass=ABCMeta):
    @abstractmethod
    def elements(self, html, source):
        pass


class LoggedCriteria(Criteria):
    def __init__(self, cls):
        self._inner = cls()

    def elements(self, html, source):
        result = list(self._inner.elements(html, source))
        name = type(self._inner).__name__

        return result


class TagCriteria(Criteria):
    def elements(self, html, source):
        tag = source.tag
        return ((x, 1) for x in html.elements(tag))


class ClassCriteria(Criteria):
    def elements(self, html, source):
        return scored(html, source, by='class')


class TitleCriteria(Criteria):
    def elements(self, html, source):
        return scored(html, source, by='title')


class OnClickCriteria(Criteria):
    def elements(self, html, source):
        return scored(html, source, by='onclick')
