import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='matrix',
    version='0.0.1',
    author='Alexey Prokhorenko',
    author_email='alexey1214@gmail.com',
    description='A small test project for Avito',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/alexey1214/matrix',
    project_urls={
        'Bug Tracker': 'https://github.com/alexey1214/matrix/issues'
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'': 'matrix'},
    packages=setuptools.find_packages(where="matrix"),
    python_requires=">=3.9",
)