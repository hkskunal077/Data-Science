# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 17:36:39 2021

@author: kushk
"""

import os
import sys

sys.path.append(os.path.abspath('scripts'))

from nyt_data import retrieve

repoURL = 'https://github.com/oreillymedia/doing_data_science/'
fileURL = 'raw/master/dds_datasets.zip'

retrieve(repoURL + fileURL, 'raw_data/')
print('Raw Data Files are succesfully retrieved')
