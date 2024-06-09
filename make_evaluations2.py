MODELS = ["meta-llama/Llama-2-7b-hf", "meta-llama/Llama-2-7b-chat-hf", "meta-llama/Meta-Llama-3-8B", "meta-llama/Meta-Llama-3-8B-Instruct"]
SHOTS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
TASK = "SMALL-MODEL"
launch_cmd = []
from itertools import product

for i, pack in enumerate(product(MODELS, SHOTS)):
    model = pack[0]
    num_shot = pack[1]
    
    task_name = pack[0].split("/")[1] + "-num-shots-" + str(pack[1])
    log_name = "/data/home/beidic/zhuoming/icl/" + task_name
    cmd1 = "accelerate launch -m lm_eval --model hf --tasks gsm8k  --batch_size 16 --model_args pretrained={}  --output_path {} --num_fewshot {}".format(model, log_name, num_shot)
    results_file = log_name + "/results.json"
    cmd2 = "cat {}".format(results_file)
    script_name = "scripts/" + task_name + "-icl{}.sh".format(TASK)
    script_cmd = """#!/bin/bash
## job name
#SBATCH --job-name={}-{}


#SBATCH --output=/data/home/beidic/zhuoming/icl/log/log-%j.out
#SBATCH --error=/data/home/beidic/zhuoming/icl/log/log-%j.err

#SBATCH --time=2:00:00 

#SBATCH -q storygen
#SBATCH -A storygen

#SBATCH --nodes=1

#SBATCH --ntasks-per-node=1

#SBATCH --cpus-per-task=20
#SBATCH --gpus-per-node=8
#SBATCH --no-requeue

source /data/home/beidic/.bashrc
source /fsx-storygen/beidic/anaconda3/etc/profile.d/conda.sh
conda activate beidic

cd /data/home/beidic/zhuoming/icl

which python 
export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 

/usr/bin/bash {}
""".format(i, task_name, cmd1)

    l_cmd = "sbatch " + script_name + "\n"
    
    launch_cmd.append(l_cmd)
    with open(script_name, "w+") as f:
        f.write(script_cmd)
    with open("submit-{}.sh".format(TASK), "w+") as f:
            f.writelines(launch_cmd)
    




    
