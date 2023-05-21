from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="Py-MLUtils",
    version="0.0.1",
    description="Library that provides various functionalities for image processing and annotation manipulation",
    package_dir={"": "ml_utilities"},
    packages=find_packages(where="ml_utilities"),
    long_description=long_description,
    url="https://github.com/gintare222/ml_utilities",
    author="Gintare Petkute",
    license="MIT",
    install_requires=['opencv-python', 'os-sys', 'typing', 'jsonlib'],
    python_requires=">=3.8",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows"
    ]
)