import os

filename = "/foo/bar/baz.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    f.write("FOOBAR")

# With the Pathlib module (introduced in Python 3.4), there is an alternate syntax (thanks David258):

from pathlib import Path
output_file = Path("/foo/bar/baz.txt")
output_file.parent.mkdir(exist_ok=True, parents=True)
output_file.write_text("FOOBAR")