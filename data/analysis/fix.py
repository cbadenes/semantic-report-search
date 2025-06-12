import nbformat

path = "32_text_generation.ipynb"

nb = nbformat.read(path, as_version=4)

if "widgets" in nb.metadata:
    del nb.metadata["widgets"]

nbformat.write(nb, path)

