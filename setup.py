from setuptools import setup, find_packages

LONG_DESCRIPTION = '''Simple Compass integration for Django.'''

CLASSIFIERS = [
                'Development Status :: 4 - Beta',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: GNU General Public License (GPL)',
                'Natural Language :: English',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Topic :: Software Development :: Libraries :: Python Modules' 
              ]

KEYWORDS = 'django sass compass css'

setup(name='django-orienteer',
    version='0.1',
    description='Django Compass App',
    long_description=LONG_DESCRIPTION,
    author='Drew Yeaton',
    author_email='drew@sentineldesign.net',
    url='http://github.com/sentineldesign/django-orienteer/',
    packages=find_packages(),
    platforms = ['Platform Independent'],
    license = 'Apache License, Version 2.0',
    classifiers = CLASSIFIERS,
    keywords = KEYWORDS,
)