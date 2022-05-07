# AiCore-Computer-Vision-Project
This project uses computer vision to implement a new version of the classic Rock Paper Scissors game. This allows the user to play against the computer
by using its computer/laptop camera.


## Milestone 1
As a first milestone for my project, I have used Teachable Machines, a web-baed tool that creates fast machine learning models. I have trained this model
with images of myself, such that it can recognises four different categories: Rock, Paper, Scissors or Nothing. I have then downloaded the trained model
with its corresponding labels to my local machine.


## Milestone 2
For the next part I have created a conda environment for my project and installed the necessary libraries and dependencies, these included:
   + opencv python - a library for computer vision
   + tenserflow - a library for machine learning & AI
   + ipykernel - a package that provides IPython kernel for Jupyter
   + 

## Milestone 3
Next, I began implementing the computer vision version of RPS by defining a class called RPS_game(). This had several methods that represent the backbone 
of this project:
   + methods that signal the start and stop acquisition for the computer camera
   + methods that record the computer's choice and the user's choice by incorporting feedback from the camera and the trained model
   + a method for determining the winner for a given round


## Milestone 4
Finally, I have define a function play_game() that makes use of the RPS_game class. In addition, it introduces another functionality that display a
countdown timer (3, 2, 1, GO!) after the start of each around. The user will display its choice after the GO! cue. Inside this function, I also determined 
that the winner will be announced after a 5-round game.

## Conclusion
I have built a computer vision project, that makes the classical RSP a bit more fun! Besides the functionality already added, future versions of this game
can benefit for additional improvements such as:
   + adding a textbox that displays round number
   + adding a textbox that display the winner for a specific round
   + adding a functionality that allows user to press 'next' on the camera display for a new round to beging 


#### Video 1: Video showing an outline of the computer vision project
https://user-images.githubusercontent.com/104773240/167257108-c34e55f6-b158-4777-96d2-cf576cd52d8a.mp4

#### Video 2: Video showing the training classes & model performance on Teachable Machine website
https://user-images.githubusercontent.com/104773240/167257135-e712aa2e-b690-4054-9983-dffa5949a10e.mp4

#### Video 3: Video showing an example RPS game
https://user-images.githubusercontent.com/104773240/167257150-2defae37-76be-4094-b055-9a63dc6f0525.mp4
