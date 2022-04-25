import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="latest-data-earthquake-indonesia",
    version="0.1",
    author="Muhammad Iqbal",
    author_email="miqbal020@hotmail.com",
    description="This is will get the latest information of earthquake in Indonesia (BMKG.go.id)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Miqbal20/latest-indonesia-earthquake-information",
    project_urls={
        "Website": "https://replit.com/@miqbal20",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ],
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)