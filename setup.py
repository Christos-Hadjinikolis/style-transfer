import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytorch-style-transfer-Christos-Hadjinikolis", # Replace with your own username
    version="0.0.1",
    author="Christos Hadjinikolis",
    author_email="christos.hadjinikolis@gmail.com",
    description="A package for doing style transfer between content_images with pytorch.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Christos-Hadjinikolis/style-transfer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)