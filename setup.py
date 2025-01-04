from setuptools import find_packages, setup

package_name = 'birthday'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kenta Ishizeki',
    maintainer_email='a.w.g.d0201@icloud.com',
    description='Birthday countdown',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'countdown = birthday.countdown:main'
        ],
    },
)
