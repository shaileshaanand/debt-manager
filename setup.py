import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="debt_management",
    version="0.0.6",
    author="Shailesh Aanand",
    author_email="anaandshailu@gmail.com",
    description="An application to manage your debts.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shaileshaanand",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=['PyQt5'],
    entry_points={'console_scripts': ['debt-manager=debt_management.debt_management:main']}
)
