#!/bin/bash
## job name
#SBATCH --job-name=11-Llama-2-7b-chat-hf-num-shots-0


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

/usr/bin/bash accelerate launch -m lm_eval --model hf --tasks gsm8k  --batch_size 16 --model_args pretrained=meta-llama/Llama-2-7b-chat-hf  --output_path /data/home/beidic/zhuoming/icl/Llama-2-7b-chat-hf-num-shots-0 --num_fewshot 0
