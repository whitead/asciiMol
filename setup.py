from setuptools import setup, find_packages

with open('./README.md') as f:
    readme = f.read()

with open('./LICENSE') as f:
    lic = f.read()

packages = find_packages()

setup(
    name='asciimol',
    version='0.1.2',
    description='An ASCII molecule viewer.',
    long_description=readme,
    author='Dominik Behrens',
    author_email='dewberryants@gmail.com',
    install_requires=['numpy'],
    url='https://github.com/dewberryants/asciimol',
    license=lic,
    packages=find_packages(exclude="docs"),
    package_data={"": ["data/*"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD 2 License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Chemistry"
    ],
)
