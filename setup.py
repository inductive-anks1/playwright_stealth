import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="playwright-stealth-custom",
    version="1.0.6",
    author="Ankit",
    author_email="ankit.kumar@plaksha.edu.in",
    description="Custom fork of playwright-stealth with extra features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/inductive-anks1/playwright_stealth",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={"playwright_stealth": ["js/*.js"]},
    python_requires='>=3, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    install_requires=[
       'playwright',
    ],
    extras_require={"test": ["pytest", ]},
)
