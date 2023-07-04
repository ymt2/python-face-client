# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import re
from distutils.core import setup

version_re = re.compile(
    r'__version__ = (\(.*?\))')

cwd = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(cwd, 'face_client', '__init__.py')) as fp:
    version = None
    for line in fp:
        if match := version_re.search(line):
            version = eval(match[1])
            break
    else:
        raise Exception('Cannot find version in __init__.py')
setup(name='face_client',
      version='.' . join(map(str, version)),
      description='face.com face recognition Python API client library',
      author='Tomaž Muraus',
      author_email='tomaz@tomaz.me',
      license='BSD',
      url='http://github.com/Kami/python-face-client',
      download_url='http://github.com/Kami/python-face-client/',
      packages=['face_client'],
      provides=['face_client'],

      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Security',
          'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
