import setuptools

packs = setuptools.find_packages()
print(packs)

setuptools.setup(
    name='change_ab',
    version='0.0.1',
    author='George Shpilevoy',
    description='Testing installation of Package',
    url='https://github.com/Hoodie-Huuuuu/change_ab',
    packages=packs
)