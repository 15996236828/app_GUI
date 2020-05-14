import os
import time
os.system("python run_classifier.py --task_name=mytask --do_predict=true --data_dir=./glue --vocab_file=../chinese_L-12_H-768_A-12/vocab.txt --bert_config_file=../chinese_L-12_H-768_A-12/bert_config.json --init_checkpoint=./mytask_output --max_seq_length=128 --output_dir=./mrpc_output")
for i in range(1000):
    i = 0
os.system("python ../get_result.py")