## Build Your Package

To publish to PyPI, you first need to build the source distribution and a wheel (binary distribution).

First, ensure that you have `setuptools` and `wheel` installed:

```bash
pip install setuptools wheel
```

Now, in the root of your project (where setup.py is located), run the following command to build the package:

```bash
python setup.py sdist bdist_wheel
```

This will generate two folders, dist/ and build/, containing your distribution files (e.g., .tar.gz and .whl).

## Upload to PyPI

To upload your package to PyPI, run the following command:

```bash
pip install twine
twine upload dist/*
```

This will install twine, the tool for securely uploading Python packages to PyPI.

> You’ll be prompted to enter your PyPI credentials, and upon successful upload, your package will be live on https://pypi.org.

## Verify Installation

To verify that your package is installed correctly, run the following command:

```bash
pip install still_alive
still-alive --help
```

If everything works as expected, congratulations! Your package is now available for others to install.

