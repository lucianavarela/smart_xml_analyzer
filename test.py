from package import app

if __name__ == '__main__':
    origin = "/home/jlight/Documents/html/sample-0-origin.html"
    button = "make-everything-ok-button"

    def run(other):
        return app.run(origin, other, button)

    # First case.
    x = run("/home/jlight/Documents/html/sample-1-evil-gemini.html")
    assert "Make everything OK" in x.inner.text
    print()

    # Second case.
    x = run("/home/jlight/Documents/html/sample-2-container-and-clone.html")
    assert "Make everything OK" in x.inner.text
    print()

    # Third case.
    x = run("/home/jlight/Documents/html/sample-3-the-escape.html")
    assert "Do anything perfect" in x.inner.text
    print()

    # Fourth case.
    x = run("/home/jlight/Documents/html/sample-4-the-mash.html")
    assert "Do all GREAT" in x.inner.text
