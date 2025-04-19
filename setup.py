from setuptools import setup, find_packages

setup(
    name='deadly',  # 项目名称
    version='1.3.3',    # 项目版本
    packages=find_packages(),  # 自动发现包
    install_requires=[],
    author='xugoudaobai',  # 作者名称
    author_email='2093289509@qq.com',  # 作者邮箱
    description='A "deadly"module in Python',  # 项目描述
    url='https://github.com/xugoudaobai/Deadly-module',  # 项目主页
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Python 版本要求
)
