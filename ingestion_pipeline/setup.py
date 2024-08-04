from setuptools import setup, find_packages

setup(
    name="ingestion_pipeline",
    version="0.1.0",
    packages=find_packages(where="src"),
    license='GPLv3',
    package_dir={"": "src"},
    install_requires=[
        "fastapi",
        "uvicorn",
        "aiohttp",
        "pyarrow",
        "pandas",
        "torch"
    ],
    author="Nicholas Dow",
    author_email="nickmingdow@gmail.com",
    description="A data ingestion pipeline with versioning and streaming capabilities",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/NicholasDow/ingestion_pipeline",
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)