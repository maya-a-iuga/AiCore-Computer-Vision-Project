# AiCore-Computer-Vision-Project
This project uses computer vision to implement a new version of the classic Rock Paper Scissors(RPS) game. In this version, the user will use his/hers computer/laptop camera to play the game with the computer as the opponent.


## Milestone 1
As a first milestone for this project, I have used Teachable Machines, a web-based tool for machine learning models. I have trained a model
with images of myself, such that the model can recognise four different image categories: Rock, Paper, Scissors or Nothing. Then, I have downloaded this trained model to my local machine.


## Milestone 2
For the next part I have created a conda environment for my project and installed the necessary libraries and dependencies:
   + opencv python - a library for computer vision
   + tenserflow - a library for machine learning & AI
   + ipykernel - a package that provides a IPython kernel for Jupyter
 

## Milestone 3
I began implementing the computer vision version of RPS by defining a class called RPS_game(). The class had several methods that represent the backbone 
of the project, namely:
   + methods that signal the start and stop of frame acquisition for the camera
   + methods that record the computer's choice and the user's choice by incorporating feedback from the camera and the trained model
   + a method for determining the winner for each round of the game


## Milestone 4
Finally, I have defined a function play_game() that incorporates methods from the RPS_game class. In addition, it introduces a new functionality that display a countdown timer (3, 2, 1, GO!) at the start of each round. The user is advised to show his/her choice after the GO! cue. Inside this function, the winner is announced after a 5 rounds game.

## Conclusion
I have built a computer vision project, that makes the classical RSP a bit more fun! Besides the functionalities already added, future versions of this game could benefit from additional improvements such as:
   + adding a textbox that displays round number
   + adding a textbox that display the winner for a specific round
   + adding a functionality that allows the user to press 'next' (on the camera display) for a new round to begin


#### Video 1: Video showing an outline of the computer vision project
https://user-images.githubusercontent.com/104773240/167257108-c34e55f6-b158-4777-96d2-cf576cd52d8a.mp4

#### Video 2: Video showing the training classes & model performance on the Teachable Machine website
https://user-images.githubusercontent.com/104773240/167257135-e712aa2e-b690-4054-9983-dffa5949a10e.mp4

#### Video 3: Video showing an example RPS game
https://user-images.githubusercontent.com/104773240/167257150-2defae37-76be-4094-b055-9a63dc6f0525.mp4
