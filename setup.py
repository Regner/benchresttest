

from pip.req import parse_requirements
from setuptools import setup, find_packages
from benchresttest import __version__

parsed_reqs = parse_requirements('requirements.txt', session=False)
install_reqs = [str(ir.req) for ir in parsed_reqs]

setup(
    name='Bench Rest Test',
    description='Entry for Bench.co rest test.',
    version=__version__,
    author='Regner Blok-Andersen',
    author_email='regnerba@gmail.com',
    url='https://github.com/Regner/benchresttest',
    packages=find_packages(),
    install_requires=install_reqs,
    entry_points='''
        [console_scripts]
        benchresttest=benchresttest.cli:cli
    ''',
)
