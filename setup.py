import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vqe_playground_006",
    version="0.0.1",
    author="James L. Weaver",
    author_email="james.l.weaver@gmail.com",
    description="Variational Quantum Eigensolver Playground",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JavaFXpert/vqe-playground",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
