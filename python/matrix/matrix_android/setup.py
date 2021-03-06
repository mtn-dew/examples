import setuptools

setuptools.setup(
    name='matrix_8x8_android',
    version='1.0',
    author='Vadym Kononenko',
    author_email='<Vadym.kononenko@gmail.com>',
    description='eKids python example 1: create a GUI application to emulate a 8x8 LED matrix',
    url="https://github.com/vadym/examples/python/matrix_8x8/matrix_8x8_android",

    packages=setuptools.find_packages(),

    # See: https://pypi.org/classifiers
    classifiers=[
        "Programming Language :: Python :: 3",

        ##
        # License choosing: http://oss-watch.ac.uk/apps/licdiff/
        #
        # 1. Popular and widely used: Yes
        # 2. Licence type: Permissive
        # 3. Jurisdiction: No
        # 4.a Grants patent rights: Yes
        # 4.b Patent retaliation clause: Yes
        # 5. Specifies enhanced attribution: No
        # 6. Addresses privacy loophole: No
        # 7. Includes 'no promotion' feature: Yes
        "License :: OSI Approved :: Apache Software License",

        "Operating System :: OS Independent",
    ],
    package_data={'Markdown': ['*.md']},
    #install_requires=[''],
    entry_points={'console_scripts': ['matrix_8x8_android = matrix_8x8_android.cli:main']},
)
