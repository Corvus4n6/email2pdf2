from setuptools import setup, find_packages
import versioneer


setup(
    name='email2pdf2',
    version=versioneer.get_version(),
    packages=find_packages(exclude=["*tests*"]),
    url='https://github.com/Corvus4n6/email2pdf2',
    license='MIT',
    author='Andrew Ferrier',
    description='email2pdf2 is a Python script to convert emails to PDF.',
    install_requires=[
        'beautifulsoup4>=4.6.3',
        'chardet',
        'html5lib',
        'lxml',
        'pypdf3',
        'python-magic',
        'reportlab',
    ],
    entry_points={
        "console_scripts": [
            'email2pdf2=email2pdf2.cmd:main'
        ]
    }
)
