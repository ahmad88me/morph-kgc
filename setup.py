import os
import re
import sys
import setuptools


CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 7)

# borrowed from urllib3
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of Morph-KGC requires Python {}.{}, but you're trying to install it on Python {}.{}.
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)


# borrowed from SQLAlchemy
with open(os.path.join(os.path.dirname(__file__), 'src', 'morph_kgc', '_version.py')) as file:
    version = (re.compile(r""".*__version__ = ["'](.*?)['"]""", re.S).match(file.read()).group(1))


with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r', encoding='utf-8') as file:
    readme = file.read()


with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as file:
    requirements = [line.strip().replace(' ', '') for line in file.readlines()]


setuptools.setup(
    name='morph_kgc',
    version=version,
    author='Julián Arenas-Guerrero',
    author_email='arenas.guerrero.julian@outlook.com',
    license='Apache 2.0',
    description='Scalable [R2]RML engine to create RDF knowledge graphs from heterogeneous data sources.',
    keywords='morph-kgc, rdf, r2rml, rml, knowledge graphs, data integration'
    ,
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/oeg-upm/Morph-KGC',
    project_urls={
        'Documentation': 'https://github.com/oeg-upm/Morph-KGC/wiki',
        'Source code': 'https://github.com/oeg-upm/Morph-KGC',
        'Issue tracker': 'https://github.com/oeg-upm/Morph-KGC/issues',
    },
    include_package_data=True,
    packages=[
        'morph_kgc',
        'morph_kgc.mapping',
        'morph_kgc.data_source',
    ],
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Pre-processors',
        'Topic :: Database',
        'Topic :: Utilities',
        'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator'
    ],
    install_requires=requirements,
    python_requires='>=3.7, <4',
)
