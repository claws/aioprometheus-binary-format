
from pip.req import parse_requirements
from pip.download import PipSession
from setuptools import setup, find_packages


install_reqs = parse_requirements("requirements.txt", session=PipSession())
requires = [str(ir.req) for ir in install_reqs]


if __name__ == "__main__":

    setup(
        name="aioprometheus-binary-format",
        version='1.0.0',
        author="Chris Laws",
        author_email="clawsicus@gmail.com",
        description="This package provides binary metrics format support for aioprometheus",
        long_description="",
        license="MIT",
        keywords=["prometheus", "monitoring", "metrics"],
        url="https://github.com/claws/aioprometheus-binary-format",
        packages=find_packages(),
        install_requires=requires)
