from setuptools import setup

requirements = [
    # package requirements go here
]

setup(
    name='JRgui',
    version='0.1.0',
    description="a GUI for JR method",
    author="Chenyang Shi",
    author_email='chenyang.shi@abbvie.com',
    url='https://github.com/curieshicy/JRgui',
    packages=['jrgui'],
    include_package_data=True,
    package_data={'jrgui': ['*.gif']},
    entry_points={
        'console_scripts': [
            'jrgui=jrgui.cli:main'
        ]
    },
    install_requires=requirements,
    keywords='JRgui',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
