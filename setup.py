from setuptools import setup,find_packages

setup(
    name='sshthru',
    version='0.1dev',
    author="Joseph Joice",
    author_email="joseph_joice@intuit.com",
    description="AWS ssh through bastion",
    packages=['sshthru'],
    entry_points = {
              'console_scripts': [
                  'sshthru = sshthru.clidriver:main',                  
              ],              
          },
    install_requires=[
        'boto3',
        'bson',
        'click',
        'configparser'
      ]
)
