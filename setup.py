from setuptools import setup, find_packages

setup(
    name="deb_cicd_prac_project",
    version="0.0.1",
    description="This contains the code in the ./src directory of the project",
    author="Shuja",
    packages=find_packages(where="./src"),
    package_dir={"": "./src"},
    install_requires=["setuptools"],
    entry_points={"packages": ["main=deb_cicd_prac_project.main:main"]},
)
