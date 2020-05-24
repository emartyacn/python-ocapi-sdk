from setuptools import setup

PACKAGE = "python-ocapi-sdk"
VERSION = "0.1.0"

classifiers = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Topic :: Software Development :: SDK',
]

install_requires = [
    "requests>=2.23.0",
]


def main():
    setup(
        name=PACKAGE,
        version=VERSION,
        description="Python SDK for Sales Force Commerce Cloud Open Commerce API",
        url="",
        author="Erik Marty",
        author_email="mhacnqa@gmail.com",
        license="Apache-2.0",
        classifiers=classifiers,
        keywords="ocapi sales force commerce cloud",
        packages=["ocapi"],
        package_dir={"ocapi": 'ocapi'},
        install_requires=install_requires,
    )


if __name__ == '__main__':
    main()