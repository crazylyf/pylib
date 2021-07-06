#!/usr/bin/env python

#================================================================
#   Copyright (C) 2021 Yufeng Liu (Braintell, Southeast University). All rights reserved.
#   
#   Filename     : image_io.py
#   Author       : Yufeng Liu
#   Date         : 2021-05-17
#   Description  : 
#
#================================================================
import SimpleITK as sitk


def load_image(imgfile):
    return sitk.GetArrayFromImage(sitk.ReadImage(imgfile))

def save_image(outfile, img):
    sitk.WriteImage(sitk.GetImageFromArray(img), outfile)
    return True

