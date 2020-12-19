import numpy as np
from snake import snakeAi
import tensorflow as tf
from generate_data_training import Generate
from statistics import mean
import csv
import numpy as np
import time
model=tf.keras.models.load_model('Model.h5')
generate=Generate()

def play():
    score_array=[]
    game_step=[]
    data_train=[]
    for j in range(1):
        game=snakeAi(gui=True)
        finished,snake,score,food=game.start()
        pre_observation=generate.get_observation(snake,food)
        step=0
        count=0
        while finished is False:
            temp_dict={}
            predictions=[]
            check=False
            # for i in range(-1,2):
            #     predict_arr=model.predict(generate.add_to_observation(pre_observation,i).reshape(1,5))[0]
            #     predictions.append(predict_arr[2])
            #     index=np.argmax(predict_arr)
            #     temp_dict[predict_arr[2]]=[i,index]

            # value=np.max(predictions)

            # while temp_dict[value][1]==0:
            #     if len(predictions)>1:
            #         predictions.remove(value)
            #         value=np.max(predictions)
            #     else:
            #         break

            for i in range(-1,2):
                predict_arr=model.predict(generate.add_to_observation(pre_observation,i).reshape(1,5))[0]
                predictions.append(predict_arr[2])
                temp_dict[predict_arr[2]]=[i,predict_arr[0]]

            value=np.max(predictions)
            if value <1e-1:
                check=True
                count+=1
            if check is False:
                while temp_dict[value][1]>0.75:
                    if len(predictions)>1:
                        predictions.remove(value)
                        value=np.max(predictions)
                    else:
                        break
                suggest_direction=temp_dict[value][0]
            else:
                suggest_direction=temp_dict[value][0]


            key=generate.get_key_type(snake,suggest_direction)
            finished,snake,score,food=game.step(key)
            if finished:
                print(count)
                print(predictions)
                print(temp_dict)
                temp=generate.add_to_observation(pre_observation,suggest_direction).tolist()
                print(suggest_direction)
                print(pre_observation)
                temp=generate.add_to_observation(pre_observation,suggest_direction).tolist()
                print(score)
                if 0 not in temp:
                    break
                temp.append(-1)
                with open('reinforcement_datav1.csv','a')as f:
                    writer=csv.writer(f,dialect='excel')
                    writer.writerow(temp)
                print("Game:",j)
                score_array.append(score)
                data_train.append(temp)
                break
            pre_observation=generate.get_observation(snake,food)
            step+=1

    #print("Mean Score:",np.max(score_array))
    #print("Mean Step:",np.max(game_step))


if __name__=="__main__":
    play()
