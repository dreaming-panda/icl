em = {'meta-llama/Llama-2-70b-hf': [0.0, 0.37373737373737376, 0.5732323232323232, 0.5555555555555556, 0.5631313131313131, 0.547979797979798, 0.5631313131313131, 0.5555555555555556, 0.5858585858585859, 0.5631313131313131], 'meta-llama/Llama-2-70b-chat-hf': [0.0, 0.1893939393939394, 0.4595959595959596, 0.5328282828282829, 0.5606060606060606, 0.5050505050505051, 0.5328282828282829, 0.5202020202020202, 0.5580808080808081, 0.5505050505050505], 'meta-llama/Meta-Llama-3-70B': [0.0, 0.5555555555555556, 0.7853535353535354, 0.8080808080808081, 0.8131313131313131, 0.8333333333333334, 0.8156565656565656, 0.8434343434343434, 0.8156565656565656, 0.8257575757575758], 'meta-llama/Meta-Llama-3-70B-Instruct': [0.0, 0.7777777777777778, 0.9166666666666666, 0.9217171717171717, 0.9040404040404041, 0.9090909090909091, 0.9166666666666666, 0.9191919191919192, 0.9141414141414141, 0.9292929292929293], 'meta-llama/Llama-2-7b-hf': [0.0, 0.050505050505050504, 0.09595959595959595, 0.12373737373737374, None, 0.1691919191919192, 0.15404040404040403, None, 0.17929292929292928, 0.13383838383838384], 'meta-llama/Llama-2-7b-chat-hf': [0.2196969696969697, 0.03787878787878788, 0.18686868686868688, None, None, 0.25, 0.255050505050505, 0.2398989898989899, 0.23232323232323232, 0.2297979797979798], 'meta-llama/Meta-Llama-3-8B': [0.0, 0.30303030303030304, 0.51010101010101, 0.5, 0.51010101010101, 0.5353535353535354, 0.48737373737373735, 0.5303030303030303, 0.5050505050505051, 0.5075757575757576], 'meta-llama/Meta-Llama-3-8B-Instruct': [0.025252525252525252, 0.7045454545454546, 0.76010101010101, 0.7803030303030303, 0.7727272727272727, 0.7752525252525253, 0.76010101010101, 0.7626262626262627, 0.7626262626262627, 0.7676767676767676]}
fm = {'meta-llama/Llama-2-70b-hf': [0.18181818181818182, 0.40404040404040403, 0.5808080808080808, 0.5580808080808081, 0.5656565656565656, 0.5505050505050505, 0.5681818181818182, 0.5656565656565656, 0.5833333333333334, 0.5707070707070707], 'meta-llama/Llama-2-70b-chat-hf': [0.4722222222222222, 0.5202020202020202, 0.5681818181818182, 0.5707070707070707, 0.5909090909090909, 0.5378787878787878, 0.5555555555555556, 0.5353535353535354, 0.5858585858585859, 0.5681818181818182], 'meta-llama/Meta-Llama-3-70B': [0.5732323232323232, 0.5606060606060606, 0.7954545454545454, 0.8181818181818182, 0.8156565656565656, 0.8333333333333334, 0.8181818181818182, 0.8459595959595959, 0.8232323232323232, 0.8257575757575758], 'meta-llama/Meta-Llama-3-70B-Instruct': [0.8762626262626263, 0.7929292929292929, 0.9191919191919192, 0.9242424242424242, 0.9065656565656566, 0.9090909090909091, 0.9166666666666666, 0.9191919191919192, 0.9141414141414141, 0.9292929292929293], 'meta-llama/Llama-2-7b-hf': [0.05555555555555555, 0.06060606060606061, 0.09595959595959595, 0.13636363636363635, None, 0.17424242424242425, 0.15656565656565657, None, 0.17929292929292928, 0.13383838383838384], 'meta-llama/Llama-2-7b-chat-hf': [0.23737373737373738, 0.2297979797979798, 0.2196969696969697, None, None, 0.25252525252525254, 0.26262626262626265, 0.2398989898989899, 0.23232323232323232, 0.23232323232323232], 'meta-llama/Meta-Llama-3-8B': [0.13131313131313133, 0.34595959595959597, 0.5176767676767676, 0.5050505050505051, 0.5176767676767676, 0.5378787878787878, 0.49242424242424243, 0.5328282828282829, 0.5050505050505051, 0.5050505050505051], 'meta-llama/Meta-Llama-3-8B-Instruct': [0.34595959595959597, 0.7323232323232324, 0.7727272727272727, 0.7828282828282829, 0.7702020202020202, 0.7777777777777778, 0.76010101010101, 0.7626262626262627, 0.76010101010101, 0.7676767676767676]}

TARGET_MODELS = ["meta-llama/Llama-2-70b-hf", "meta-llama/Llama-2-70b-chat-hf", "meta-llama/Meta-Llama-3-70B", "meta-llama/Meta-Llama-3-70B-Instruct"]
DRAFT_MODELS = ["meta-llama/Llama-2-7b-hf", "meta-llama/Llama-2-7b-chat-hf", "meta-llama/Meta-Llama-3-8B", "meta-llama/Meta-Llama-3-8B-Instruct"]

import matplotlib.pyplot as plt

def draw_em(idx:int):
    TM = TARGET_MODELS[idx]
    DM = DRAFT_MODELS[idx]
    tm_score = []
    dm_score = []
    num_shot = []
    for i, score in enumerate(em[DM]):
        if score is not None and em[TM][i] is not None:
            dm_score.append(score)
            tm_score.append(em[TM][i])
            num_shot.append(i)
    
    pic_name = "pictures/" + TM.split("/")[1] + "-em"
    pic_title = TM.split("/")[1] + "-" + DM.split("/")[1]
    
    plt.figure(figsize=(20, 10), dpi=100)
    plt.plot(num_shot, dm_score, c="blue", label="draft")
    plt.plot(num_shot, tm_score, c="red", label="target")
    plt.legend()
    plt.title(pic_title)
    plt.savefig(pic_name +".pdf")
    plt.clf()

def draw_fm(idx:int):
    TM = TARGET_MODELS[idx]
    DM = DRAFT_MODELS[idx]
    tm_score = []
    dm_score = []
    num_shot = []
    for i, score in enumerate(fm[DM]):
        if score is not None and fm[TM][i] is not None:
            dm_score.append(score)
            tm_score.append(fm[TM][i])
            num_shot.append(i)
    
    pic_name = "pictures/" + TM.split("/")[1] + "-fm"
    pic_title = TM.split("/")[1] + "-" + DM.split("/")[1]
    
    plt.figure(figsize=(20, 10), dpi=100)
    plt.plot(num_shot, dm_score, c="blue", label="draft")
    plt.plot(num_shot, tm_score, c="red", label="target")
    plt.legend()
    plt.title(pic_title)
    plt.savefig(pic_name +".pdf")
    plt.clf()

for i,m in enumerate(TARGET_MODELS):
    draw_em(i)
    draw_fm(i)
    
    