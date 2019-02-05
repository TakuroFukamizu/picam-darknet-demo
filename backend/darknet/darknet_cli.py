# -*- coding: utf-8 -*-

import os
import re
import subprocess
import argparse

from backend.configs import ROOT_DIR, DARKNET_PATH
from .yolo_config import YoloConfig

def run_command(cmd: list):
    # p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # p = subprocess.Popen(cmd, shell=False, bufsize=-1, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
    p = subprocess.Popen(cmd, shell=False, bufsize=-1, close_fds=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_data, stderr_data = None, None
    try:
        stdout_data, stderr_data = p.communicate(timeout=30)
    except KeyboardInterrupt:
        print('Ctrl C')
        print(stdout_data, stderr_data)
    except Exception as ex:
        raise ex
    # stdout_data, stderr_data = p.communicate(timeout=30)
    print('stdout_data', type(stdout_data))
    print('stderr_data', type(stderr_data))

    def convert_outputs(output: bytes):
        x = output.decode(encoding='utf-8')
        x = str(x).split('\n')
        return x

    stdout_data = convert_outputs(stdout_data)
    stderr_data = convert_outputs(stderr_data)

    return p.returncode, stdout_data, stderr_data

def exec_darknet(config: YoloConfig, image_path: str):
    main_workdir = os.getcwd()

    os.chdir(DARKNET_PATH)
    print('currend dir:', os.getcwd())

    pattern_error_cannot_load_image = 'Cannot load image "([\w/-]+)"' #'Cannot load image "/home/pi/my_picture.jpg"'
    pattern_stb_reason = 'STB Reason: (.+)'  #"STB Reason: can't fopen"
    repatter_stb_reason = re.compile(pattern_stb_reason)

    pattern_predict_finish = '[\w/-]+.jpg: Predicted in ([0-9.]+) seconds.'
    repatter_predict_finish = re.compile(pattern_predict_finish)

    pattern_predict_item = '([\w-]+): ([0-9.]+)%'
    repatter_predict_item = re.compile(pattern_predict_item)

    # ret, stdout, stderr = run_command(
    #     './darknet detector test {dataset} {config} {weights} {image}'.format(
    #         dataset=config.dataset_file,
    #         config=config.config_file,
    #         weights=config.weights_file,
    #         image=image_path
    #     ),
    #     cwd=DARKNET_PATH
    #     )
    # ret, stdout, stderr = run_command(
    #     '{base}/darknet detector test {dataset} {config} {weights} {image}'.format(
    #         base=DARKNET_PATH,
    #         dataset=config.dataset_file,
    #         config=config.config_file,
    #         weights=config.weights_file,
    #         image=image_path
    #     ))
    os.environ['PATH'] = '{}:{}'.format(DARKNET_PATH, os.environ['PATH'])
    print(os.environ['PATH'])
    print(os.path.join(DARKNET_PATH, 'darknet'), os.path.exists(os.path.join(DARKNET_PATH, 'darknet')))
    print(config.dataset_file, os.path.exists(config.dataset_file))
    print(config.config_file, os.path.exists(config.config_file))
    print(config.weights_file, os.path.exists(config.weights_file))
    print(image_path, os.path.exists(image_path))
    ret, stdout, stderr = run_command(['./darknet', 'detector', 'test', config.dataset_file, config.config_file, config.weights_file, image_path])
    
    
    # エラーチェック
    for line in stderr:
        result = repatter_stb_reason.match(line)
        if result:
            reason = result.group(1)
            raise Exception(reason)

    # 認識結果の確認
    was_predicted = False
    predicted_results = []
    if len(stdout) > 0:
        for line in stdout:
            if not was_predicted:
                result = repatter_predict_finish.match(line)
                if result:
                    elapsed_time = float(result.group(1))
                    fps = 1.0 / elapsed_time
                    print(result.group(), '{} FPS'.format(fps))
                    was_predicted = True
            else:  # 認識結果
                result = repatter_predict_item.match(line)
                if result:
                    class_label = result.group(1)
                    prod = int(result.group(2)) / 100
                    predicted_results.append((class_label, prod))
                else:
                    print('invalid line', line)
    return predicted_results

if __name__ == '__main__':
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    predicted_results = exec_darknet('data/person.jpg')
    print(predicted_results)
    
