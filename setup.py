import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME = "Text_Summarizer_Project"
AUTHOR_NAME = "Ravi Agrawal"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL = "ra921741@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ra921741/Text_Summarizer_Project",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis"]
)
    

