try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Hello, How are you?',
    'author': 'Myself',
    'url': 'hello@howryou.org',
    'download_url': 'myname$me.org',
    'author_email': 'myself654@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['HUMAN'],
    'scripts': [],
    'name': 'BONE'
}


setup(**config)
