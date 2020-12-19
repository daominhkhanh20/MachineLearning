## Idea for project
 - 1: By using neural network, Snake can be learned to eat the most apple by themselves
 - 2:But we need the data for neural, we initialize data by having the snake play itself or you can play snake for generate data(about 40 game).
  We need about 20000 data point for training.But one thing that I went to remind you is the dataset need to the balance for 3 label -1,0,1.Because at the past time,I have one data set has 10032 labels 1,5832 labels 0 and only 121 labels -1.So the model doesn't work perfectly. <br>
   Each data point has 6 value:
     - Block left: 1 or 0
     - Block forward: 1 or 0
     - Block right: 1 or 0
     - Angle between snake head and apple(we need normalize the angle between -1 and 1)
     - Suggest direction:
         - -1:Go left
         -  0:Go forward
         -  1:Ggo right
     - Decision:
         - -1:Snake dead
         -  0:Snake survive but make the wrong decision
         -  1:Snake make good decision

 - 3:Neural network architecture:
     - Inpute layer: 6 Node(include bias)
     - The first hidden layer:
         - 10 Neuron (include bias)
         - Actiovation= Rectified Linear Unit
     - The second hidden layer:
         - 16 Neuron (include bias)
         - Actiovation= Rectified Linear Unit
     - Output layer:
         - 3 Node: -1,0,1
         - Activation= Softmax

## Choose the decision
- At each time, the snake has one state: block left, block right, block front, angle, and 3 direction.
So base on the state and 3 directions, you will predict the right direction for the snake. But what the right direction?
I define the right direction is nearer the food, you can define the rule for your game.
- But we have 3 input ==> 3 output.Each output has 3 value, each value is probability for
snake can died,move wrong direction,move good direction.But the direction has small distance from snake head to food
isn's sure whether colision with barrier or snake body.
- Asusuming that
 - If we move each direction,output is $[a_1,a_2,a_3]$

 I choose the direction which satisfied the following rules:
  - Step 1: We choos the direction which has max $a_3$
  - Step 2:If 0.1< $a_3$,move step 4
  - Step 3:If 0.1 > $a_3$, we remove the direction we choose in the last time,move step 1.
  Because if we choos this direction, It could lead to a dead end.
  - Step 4:Move



