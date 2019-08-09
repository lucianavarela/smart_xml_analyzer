import sys
import os.path

from .html import Html, HtmlElementPattern
from .search import LoggedCriteria, ClassCriteria, TitleCriteria, OnClickCriteria


def run(origin, other):
    element_id = 'make-everything-ok-button'
    print(f"Searching in file named [ {os.path.basename(other)} ].")

    origin_html = Html(origin)
    other_html = Html(other)

    element = HtmlElementPattern.of(origin_html, id=element_id)
    element = element.find_in(other_html,
                              LoggedCriteria(ClassCriteria),
                              LoggedCriteria(TitleCriteria),
                              LoggedCriteria(OnClickCriteria))

    print("Path: " + element.path)

    return element


if __name__ == '__main__':
    py, origin, other, element_id = sys.argv

    x = run(origin, other, element_id)
