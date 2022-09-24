import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-package",
    author="WANG Hailin",
    author_email="hailin.wang@connect.polyu.hk",
    description="Type hints for Abaqus/Python scripting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/haiiliin/python-package",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'Bug Tracker': 'https://github.com/haiiliin/python-package/issues',
        'Documentation': 'https://python-package.haiiliin.com',
        'Anaconda': 'https://anaconda.org/haiiliin/python-package',
        'Read the Docs': 'https://readthedocs.org/projects/python-package',
    },
    use_scm_version={
        "root": ".",
        "relative_to": __file__,
        "local_scheme": "node-and-date",
        "write_to": "python_package/_version.py",
        "fallback_version": "0.0.1-unknown",
    },
    setup_requires=['setuptools_scm'],
    python_requires='>=3.7',
    install_requires=['setuptools_scm'],
    packages=setuptools.find_packages('.'),
)
