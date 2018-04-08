import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='predictor',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='A Django application to predict horse races.',
    author='John Condon',
    author_email='johnnycndn@gmail.com',
    
    install_requires=['Django>=2.0.2',
                      'beautifulsoup4>=4.6.0',
                      'selenium>=3.9.0',
                      'requests>=2.18.4'],
    
    
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0.2',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)