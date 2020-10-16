import setuptools

def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description


setuptools.setup(
    name='py3rosmsgs',
    version='1.17',
    author="Rahul Bhadani",
    author_email="rahulbhadani@email.arizona.edu",
    description="Python 3 Port of ROS 1.0 messages from genpy generated python classes and pre-compiled binaries.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'pyserial',
        'pathlib',
        'gnupg'
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Robot Framework",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: MIT License",
        ],
    keywords='autonomous vehicle, ACC, adaptive cruise control, robotics, ros, visualization',
    include_package_data=True,
    zip_safe=False
        )
