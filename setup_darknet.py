# -*- coding: utf-8 -*-

import sys
import os
import shutil
from backend.configs import ROOT_DIR
from backend.configs import USER_DARKNET_LABEL_FILE, USER_DARKNET_CONFIG_FILE, USER_DARKNET_WEIGHT_FILE
from backend.configs import DARKNET_LABEL_FILE, DARKNET_CONFIG_FILE, DARKNET_WEIGHT_FILE, DARKNET_DATASET_FILE

if __name__ == "__main__":
    file_list = [
        (USER_DARKNET_LABEL_FILE, DARKNET_LABEL_FILE),
        (USER_DARKNET_CONFIG_FILE, DARKNET_CONFIG_FILE),
        (USER_DARKNET_WEIGHT_FILE, DARKNET_WEIGHT_FILE),
    ]

    for from_file, to_file in file_list:
        try:
            dir_path, _ = os.path.split(to_file)
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)
            shutil.copyfile(from_file, to_file)
        except shutil.SameFileError as ex:
            pass
        except Exception as ex:
            raise ex
    
    with open(DARKNET_DATASET_FILE, 'w') as data_file:
        body = '''classes=1
train=temp/train/index.txt
valid=temp/val/index.txt
backup=backup/
names=manacamera/labels.txt
        '''
        # TODO: template化
        data_file.write(body)
