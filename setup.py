from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="yolobel",
    version="0.0.3",
    description="Video and Image labeling tool for YOLO",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/enisgetmez",
    author="Enis Getmez",
    author_email="enis@enisgetmez.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    packages=["yolobel"],
    include_package_data=True,
     install_requires=[            
          'numpy',
          'opencv-python'
      ],
   entry_points={
        "console_scripts": [
            "yolobel=yolobel.yolobel:register_window",
        ]
    },
)