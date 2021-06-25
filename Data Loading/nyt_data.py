# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 17:27:57 2021

@author: kushk
"""

import requests, zipfile, io, shutil

unpackedFolder = 'dds_datasets/'
unpackedZipFile = 'dds_ch2_nyt.zip'

def retrieve(sourceFile, destinationFolder):
    def cleanup():
        try:
            shutil.rmtree(destinationFolder+unpackedFolder)
        except OSError as e:
            print("Folder: %s, Error: %s"%(e.filename, e.strerror))
    
    r = requests.get(sourceFile)
    assert r.status_code == requests.codes.ok
    
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(destinationFolder)
    
    z = zipfile.ZipFile(destinationFolder+unpackedFolder+unpackedZipFile)
    z.extractall(destinationFolder)
    
    cleanup()
    
    