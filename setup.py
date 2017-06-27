from setuptools import setup,find_packages

setup(
    name='sshthru',
    version='0.1dev',
    author="Joseph Joice",
    author_email="joseph_joice@intuit.com",
    description="AWS ssh through bastion",
    package_dir={'': 'sshthru'},
    packages=find_packages("sshthru")
)
