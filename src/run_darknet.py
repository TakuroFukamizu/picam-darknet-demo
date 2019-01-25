
import os
import re
import subprocess
from configs import ROOT_DIR, DARKNET_PATH

def run_command(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_data, stderr_data = p.communicate()
    return p.returncode, stdout_data, stderr_data

if __name__ == '__main__':
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    main_workdir = os.getcwd()

    os.chdir(DARKNET_PATH)

    pattern_predict_finish = '[\w/-]+.jpg: Predicted in ([0-9.]+) seconds.'
    repatter_predict_finish = re.compile(pattern_predict_finish)

    pattern_predict_item = '([\w-]+): ([0-9.]+)%'
    repatter_predict_item = re.compile(pattern_predict_item)

    ret, stdout, stderr = run_command('./darknet detector test cfg/coco.data cfg/yolov3-tiny.cfg yolov3-tiny.weights data/person.jpg')
    if len(stdout) > 0:
        print("## stdout")
        print(stdout)
    if len(stderr) > 0:
        print("## stderr")
        print(stderr)

    was_predicted = False
    predicted_results = []
    for line in str(stdout).split('\n'):
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
    print(predicted_results)


# with open(os.path.join(root_dir, 'darknet_detecotr_test_out1.txt')) as f:
#     was_predicted = False
#     predicted_results = []
#     for line in f:
#         if not was_predicted:
#             result = repatter_predict_finish.match(line)
#             if result:
#                 elapsed_time = float(result.group(1))
#                 fps = 1.0 / elapsed_time
#                 print(result.group(), '{} FPS'.format(fps))
#                 was_predicted = True
#         else:  # 認識結果
#             result = repatter_predict_item.match(line)
#             if result:
#                 class_label = result.group(1)
#                 prod = int(result.group(2)) / 100
#                 predicted_results.append((class_label, prod))
#             else:
#                 print('invalid line', line)
#     print(predicted_results)
        
