import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='file_synchronization',  
    version='0.1',
    author="xiaojueguan",
    author_email="xiaojueguan@gmail.com",
    description="A file synchronization package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/albertjone/file_synchronization",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['directory', 'folder', 'update', 'synchronisation'],
    python_requires='>=3.6'
 )