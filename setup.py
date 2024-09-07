from setuptools import setup, find_packages

setup(
    name="still_alive",  # Package name
    version="1.1.1",  # Version
    packages=find_packages(),  # Automatically find the package
    install_requires=[
        "pyautogui",  # Add dependencies here
    ],
    entry_points={
        'console_scripts': [
            'still-alive=still_alive.mouse_mover:main',  # Command to run your script
        ],
    },
    author="pythonpioneer",
    author_email="kumarhritiksinha@gmail.com",
    description="A Command-line tool that moves the mouse slightly at regular intervals",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pythonpioneer/Still-Alive",  # Project URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
    ],
    python_requires='>=3.6',
)
