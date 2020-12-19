import numpy as np
from random import randint
from math import acos, pi,atan2,sqrt
from snake import snakeAi
import pygame

class Generate:
    def __init__(self, initial_games=5, test_games=100, global_steps=100000, lr=1e-3):
        self.initial_games = initial_games  # number of game for training data
        self.test_games = test_games  # number test after training model
        self.global_steps = global_steps  # maximum number of move steps in each games
        self.lr = lr  # learn rate
        sizeBlock=snakeAi().get_sizeBlock()
        self.vector_keys = [[[-sizeBlock, 0], 0],  # go left
                            [[0, sizeBlock], 1],  # go down
                            [[sizeBlock, 0], 2],  # go right
                            [[0, -sizeBlock], 3]]  # go up



    # def generate_data(self):
    #     '''
    #     +Each element in training data is a list:
    #        *) Fist element in list is n-array has 5 atribute:
    #           -block left: 1 or 0
    #           -block right:1 or 0
    #           -block forward:1 or 0
    #           -angle after normolize:between apple and snake
    #           -suggest direction: -1(left),0(forward),1(right)
    #         *) Second element in list is integer:
    #            - -1:snake died
    #            -  0:snake survive but make the wrong decision
    #            -  1: snake survive and make a good decision
    #     '''
    #     training_data = []
    #     for j in range(self.initial_games):
    #         print("-----")
    #         print("Game: ", j)
    #         game = snakeAi(gui=True)
    #         _, snake, _, food = game.start()


    #         pre_observation = self.get_observation(snake, food)
    #         pre_distance_food = self.get_distance_food(snake, food)
    #         for _ in range(self.global_steps):
    #             suggest_direction, key_type = self.get_action(snake)
    #             finished, snake, _, food = game.step(key_type)
    #             if finished:
    #                 # if died, then label is -1
    #                 temp=generate.add_to_observation(pre_observation, suggest_direction).tolist()
    #                 temp.append(-1)
    #                 print(temp)
    #                 training_data.append(temp)
    #                 break

    #             else:
    #                 distance = generate.get_distance_food(snake, food)
    #                 if distance >pre_distance_food:
    #                     # if snake still survived,but distance from head snake is more far than pre-observation
    #                     temp=generate.add_to_observation(pre_observation, suggest_direction).tolist()
    #                     temp.append(0)
    #                     print(temp)
    #                     training_data.append(temp)

    #                 else:
    #                     temp=generate.add_to_observation(pre_observation, suggest_direction).tolist()
    #                     temp.append(1)
    #                     print(temp)
    #                     training_data.append(temp)

    #             pre_observation = self.get_observation(snake, food)
    #             pre_distance_food = distance

    #     return training_data

    def add_to_observation(self, observation, direction):
        return np.append(observation, [direction])

    def get_action(self, snake):
        suggest_direction = randint(-1, 1)
        return suggest_direction, self.get_key_type(snake, suggest_direction)

    def get_key_type(self, snake, suggest_direction):
        key=0
        snake_direction = self.get_snake_direction(snake)
        new_direction = snake_direction
        if suggest_direction == -1:
            new_direction = self.turn_vector_to_left(snake_direction)
        elif suggest_direction == 1:
            new_direction = self.turn_vector_to_right(snake_direction)
        new_direction = new_direction.tolist()

        for pair in self.vector_keys:
            if pair[0] == new_direction:
                key = pair[1]

        return key

    def is_block_barrier(self,direction):
        x,y=direction
        width,height=snakeAi().get_sizeScreen()
        if x < 0 or y < 0 or x >=width or y >= height:
            return True
        return False

    def is_collision_body(self,snake,direction):
        if direction in snake[1:]:
            return True
        return False

    def is_block(self, snake, direction):
        new_direction = np.array(snake[0]) + direction
        c=True
        if self.is_collision_body(snake,new_direction.tolist()) or self.is_block_barrier(new_direction.tolist()):
            c=False


        if c == False:
            return 1
        return 0

    def get_observation(self, snake, food):
        snake_direction = self.get_snake_direction(snake)
        food_direction = self.get_food_direction(snake, food)
        block_left = self.is_block(
            snake, self.turn_vector_to_left(snake_direction))
        block_right = self.is_block(
            snake, self.turn_vector_to_right(snake_direction))
        block_forward = self.is_block(snake, snake_direction)
        angle = self.get_angle(snake_direction, food_direction)
        return np.array([block_left,block_forward,block_right,angle])

    def turn_vector_to_left(self, vector):
        return np.array([vector[1], -vector[0]])

    def turn_vector_to_right(self, vector):
        return np.array([-vector[1], vector[0]])

    def get_snake_direction(self, snake):
        return np.array(snake[0]) - np.array(snake[1])

    def get_food_direction(self, snake, food):
        return np.array(food) - np.array(snake[0])

    def get_distance_food(self, snake, food):
        return np.linalg.norm(self.get_food_direction(snake, food))

    def normalized_vector(self, anpha):
        norm=np.linalg.norm(anpha)
        if norm==0:
            return (0,0)

        return anpha/norm

    def get_angle(self, a, b):
        x1,y1= self.normalized_vector(a)
        x2,y2 = self.normalized_vector(b)
        if x2==0 and y2==0:
            return 0
        '''
        |A.B|=|A|.|B|.cos(phi)
        |A*B|=|A|.|B|.sin(phi)

        '''
        return atan2(x1*y2-x2*y1,x1*y1+x2*y2)/pi

    def get_suggest_direction(self,snake,key):
        x,y=self.get_snake_direction(snake)
        vector_keys=self.vector_keys
        step=[0,0]
        for pair in vector_keys:
            if key==pair[1]:
                step=pair[0]
                break

        if step==[y,-x]:
            return -1
        elif step==[-y,x]:
            return 1

        return 0


train_data=[]
generate=Generate()



if __name__ == "__main__":

    i=0
    while i <40:
        game = snakeAi(gui=True)
        finished, snake, pre_score, food = game.start()
        button_direction = 1
        pre_direction = 1
        pre_observation=generate.get_observation(snake,food)
        pre_distance_food=generate.get_distance_food(snake,food)

        while finished is False:
            for event in pygame.event.get():
                if event.type == pygame.K_END:
                    finished = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and pre_direction != 2:
                        button_direction = 0
                    elif event.key == pygame.K_DOWN and pre_direction != 3:
                        button_direction = 1
                    elif event.key == pygame.K_RIGHT and pre_direction != 0:
                        button_direction = 2
                    elif event.key == pygame.K_UP and pre_direction != 1:
                        button_direction = 3
                    else:
                        button_direction = button_direction


            suggest_direction=generate.get_suggest_direction(snake,button_direction)
            finished, snake,score,food = game.step(button_direction,i+1)

            if finished:
                temp=generate.add_to_observation(pre_observation, suggest_direction).tolist()
                temp.append(-1)
                print(temp)
                train_data.append(temp)
                break

            else:
                distance = generate.get_distance_food(snake, food)
                if distance <pre_distance_food :
                    # if snake still survived,but distance from head snake is more far than pre-observation
                    temp=generate.add_to_observation(pre_observation, suggest_direction).tolist()
                    temp.append(1)
                    print(temp)
                    train_data.append(temp)

                else:
                    temp=generate.add_to_observation(pre_observation, suggest_direction).tolist()
                    temp.append(0)
                    print(temp)
                    train_data.append(temp)

                pre_observation = generate.get_observation(snake, food)
                pre_distance_food = distance

            pre_direction = button_direction

        i+=1

    data=np.asarray(train_data)
    np.savetxt('data1.csv',data,delimiter=',')

