import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="danmu_utils",
    version="2.3.0",
    author="Example Author",
    author_email="hawthorn7dd@hotmail.com",
    description="Danmu utils support download and convert danmu.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hawthorn2013/danmu_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)