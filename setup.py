from setuptools import setup, find_packages

setup(name='python-console-snake',
      version='0.1',
      description='Lightweight, configurable snake game running in the console',
      url='https://github.com/tancredi/python-console-snake',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'snake=snake.main:run',
          ]
      })
