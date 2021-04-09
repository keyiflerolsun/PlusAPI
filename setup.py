# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from setuptools import setup
from io import open

with open(f'requirements.txt') as dosya:
    GEREKSINIM = dosya.read().splitlines()

setup(
    author       = 'keyiflerolsun',
    author_email = 'keyiflerolsun@gmail.com',

    packages     = ['PlusAPI'],

    name         = 'PlusAPI',
    version      = '0.0.1',
    url          = 'https://github.com/keyiflerolsun/PlusAPI',
    description  = 'PlusAPI | Piyasa Verileri | Python',
    keywords     = 'PlusAPI',

    long_description_content_type   = "text/markdown",
    long_description                = "".join(open("README.md", encoding="utf-8").readlines()),
    include_package_data            = True,

    license     = 'GPLv3+',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3'
    ],

    python_requires     = '>=3.6',
    install_requires    = GEREKSINIM
)
