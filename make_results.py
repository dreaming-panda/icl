MODELS = ["meta-llama/Llama-2-70b-hf", "meta-llama/Llama-2-70b-chat-hf", "meta-llama/Meta-Llama-3-70B", "meta-llama/Meta-Llama-3-70B-Instruct"
          ,"meta-llama/Llama-2-7b-hf", "meta-llama/Llama-2-7b-chat-hf", "meta-llama/Meta-Llama-3-8B", "meta-llama/Meta-Llama-3-8B-Instruct"]
SHOTS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
TASK = "LARGE-MODEL"
import json
launch_cmd = []
from itertools import product
import os
strict_match = {}
flexible_match = {}
for m in MODELS:
    strict_match[m] = [None for _ in SHOTS]
    flexible_match[m] = [None for _ in SHOTS]
for i, pack in enumerate(product(MODELS, SHOTS)):
    model = pack[0]
    num_shot = pack[1]
    
    task_name = pack[0].split("/")[1] + "-num-shots-" + str(pack[1])
    log_name = "/data/home/beidic/zhuoming/icl/" + task_name
    results_file = log_name + "/results.json"
    if not os.path.exists(results_file):
        continue
    with open(results_file, "r") as log:
        result_dict = json.load(log)
        em = result_dict["results"]["gsm8k"]["exact_match,strict-match"]
        fm = result_dict["results"]["gsm8k"]["exact_match,flexible-extract"]
        strict_match[model][num_shot] = em
        flexible_match[model][num_shot] = fm

print(strict_match)
print(flexible_match)
        
    
    

    
