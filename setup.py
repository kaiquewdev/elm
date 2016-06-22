import os
import glob
from setuptools import setup

import versioneer

version = versioneer.get_version()
cmdclass = versioneer.get_cmdclass()

setup(name='iamlp',
      version=version,
      cmdclass=cmdclass,
      description='Image Analysis Machine Learning Pipeline',
      packages=['iamlp',
                'iamlp.acquire',
                'iamlp.config',
                'iamlp.data_selectors',
                'iamlp.ensemble',
                'iamlp.model_selectors',
                'iamlp.partial_fit',
                'iamlp.pipeline',
                'iamlp.preproc',
                'iamlp.readers',
                'iamlp.scripts',
                'iamlp.writers',
                ],
      data_files=[],
      entry_points={
        'console_scripts': [
            'iamlp-download-ladsweb = iamlp.acquire.ladsweb_ftp:main',
            'iamlp-main = iamlp.scripts.main:main'

        ]},)