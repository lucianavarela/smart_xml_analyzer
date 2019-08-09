from package import app

if __name__ == '__main__':
    origin = "test_files/sample-0-origin.html"

    def run(other):
        return app.run(origin, other)

    # First case.
    x = run("test_files/sample-1-evil-gemini.html")
    assert "Make everything OK" in x.inner.text
    print()

    # Second case.
    x = run("test_files/sample-2-container-and-clone.html")
    assert "Make everything OK" in x.inner.text
    print()

    # Third case.
    x = run("test_files/sample-3-the-escape.html")
    assert "Do anything perfect" in x.inner.text
    print()

    # Fourth case.
    x = run("test_files/sample-4-the-mash.html")
    assert "Do all GREAT" in x.inner.text
