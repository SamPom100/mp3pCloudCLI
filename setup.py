from setuptools import setup, find_packages

setup(
    name='mp3-pcloud-cli',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mp3-pcloud-cli=module.main:main',
        ],
    },
    install_requires=[
        'requests',
        'yt-dlp',
    ],
)
