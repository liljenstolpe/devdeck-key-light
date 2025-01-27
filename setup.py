from setuptools import setup, find_packages
import subprocess

from xdg.BaseDirectory import *

def get_version():
    process = subprocess.Popen(["git", "describe", "--always", "--tags"], stdout=subprocess.PIPE, stderr=None)
    last_tag = process.communicate()[0].decode('ascii').strip()
    if '-g' in last_tag:
        return last_tag.split('-g')[0].replace('-', '.')
    else:
        return last_tag

assetsDir = os.path.join(xdg_config_home, 'devdeck/assets')
print(assetsDir)

with open('requirements.txt') as f:
    install_reqs = f.read().splitlines()

setup(
    name='devdeck_key_light',
    version=get_version(),
    description="Elgato Key Light controls for DevDeck.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='James Ridgway',
    url='https://github.com/jamesridgway/devdeck-key-light',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_reqs,
    data_files=[(str(assetsDir), ['assets/key-light-on.png','assets/key-light-off.png'])]
)
