from pathlib import Path

from setuptools import setup


NAME = 'MSS'
DESCRIPTION = 'Music source separation'

URL = 'https://github.com/matttic97/Music-Source-Separation-Training'
EMAIL = ''
AUTHOR = 'Roman Solovyev (ZFTurbo): https://github.com/ZFTurbo/'
REQUIRES_PYTHON = '>=3.8.0'

HERE = Path(__file__).parent
VERSION = '1.0.0'


def load_requirements(name):
    required = [i.strip() for i in open(HERE / name)]
    required = [i for i in required if not i.startswith('#')]
    return required


REQUIRED = load_requirements('requirements.txt')
ALL_REQUIRED = load_requirements('requirements.txt')

try:
    with open(HERE / "README.md", encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=['Music-Source-Separation-Training'],
    extras_require={
        'dev': ALL_REQUIRED,
    },
    install_requires=REQUIRED,
    include_package_data=True
)