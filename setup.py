import setuptools

with open("Readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

print("====Listing packages found:====")
print(setuptools.find_packages())
print("===============================")
setuptools.setup(
    name="bmark",
    version="1.0",
    description="Benchmark dataset curation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
)
