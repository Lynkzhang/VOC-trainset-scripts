import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets=['trainval',  'val',  'train']

#classes = [""]



wd = getcwd()

for image_set in sets:
    image_ids = open('ImageSets/Segmentation/%s.txt'%(image_set)).read().strip().split()
    list_file = open('%s.txt'%(image_set), 'w')
    label_file= open('label_%s.txt'%(image_set), 'w')
    for image_id in image_ids:
        list_file.write('/home/Lynkzhang/VOCdevkit/VOC2012/JPEGImages/%s.jpg\n'%( image_id))
	label_file.write('/home/Lynkzhang/VOCdevkit/VOC2012/SegmentationClass/%s.png\n'%( image_id))
    list_file.close()


