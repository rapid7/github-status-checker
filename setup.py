from setuptools import setup, find_packages

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name="github_status_checker",
    version="1.0.1",
    description="Python module/tool for checking the status of GitHub.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Rapid7 Integration Alliance',
    author_email='integrationalliance@rapid7.com',
    url='https://github.com/rapid7/github-status-checker',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        "requests~=2.0"
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'github-status=github_status_checker.__main__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Version Control :: Git",
        "Topic :: System :: Networking :: Monitoring"
      ],
)
