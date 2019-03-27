import os
import datetime
import shutil
import csv

from backend.darknet import exec_darknet, YoloConfig
from backend.camera import capture

def detect(config: YoloConfig, img_path: str):
    # net = load_net(config.config_file, config.weights_file, 0)
    # meta = load_meta(config.dataset_file)
    # r = detect(net, meta, img_path)
    # .so is not working now.
    r = exec_darknet(config, img_path)
    return r

def prep_output_dir(output_root_dir: str):
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y%m%d-%H%M%S')
    output_dir = os.path.join(output_root_dir, timestamp)

    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def capture_and_logging(config: YoloConfig, output_root_dir: str, capture_time: int = 3):

    output_dir = prep_output_dir(output_root_dir)

    results = []
    result_images = []
    keys = []
    for _ in range(capture_time):
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y%m%d-%H%M%S')

        file_path = capture()
        resutls = detect(config, file_path)
        for class_label, prod in resutls:
            results.append((timestamp, class_label, prod))
            print(timestamp, class_label, prod)
        result_images.append((timestamp, file_path))
        keys.append(timestamp)
    print(len(results))

    total_csv = os.path.join(output_root_dir, 'total.csv')
    for key in keys:
        results_filterd = []
        image_file = None
        for timestamp, class_label, prod in results:
            if timestamp == key:
                results_filterd.append((timestamp, class_label, prod))
        for timestamp, file_path in result_images:
            if timestamp == key:
                image_file = file_path

        num_of_person = len(results_filterd)

        # 画像をコピー
        image_file = shutil.move(image_file, output_dir)

        # 個別フォルダに詳細CSVを出力
        predicts_csv = os.path.join(output_dir, '{}_predicts.csv'.format(key))
        try:
            with open(predicts_csv, 'w') as csvfile:
                writer = csv.writer(csvfile, lineterminator='\n')
                for timestamp, class_label, prod in results_filterd:
                    writer.writerow([timestamp, class_label, prod])
        except FileNotFoundError as e:
            print(e)
        except csv.Error as e:
            print(e)
        
        # 全体のCSVに追記
        try:
            with open(total_csv, 'a') as csvfile:
                writer = csv.writer(csvfile, lineterminator='\n')
                writer.writerow([key, num_of_person, image_file])
        except FileNotFoundError as e:
            print(e)
        except csv.Error as e:
            print(e)

        
