from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="streamlit-tree-select-community",
    version="0.1.1",
    author="Thilina Jayawardana",
    author_email="",
    description="A community-maintained checkbox tree component for Streamlit.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thilina227/streamlit_tree_select",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
