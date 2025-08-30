from setuptools import setup, find_packages

setup(
    name="fipiran-nav",
    version="1.0.0",
    author="Kimi2 Salehy Delarestaghy",
    author_email="kimiaslhd@gmail.com",
    description="Simple library to fetch Iranian fund data",
    url="https://github.com/Kimiaslhd/fipiran_nav",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
)