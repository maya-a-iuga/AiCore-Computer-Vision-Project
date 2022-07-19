import cv2
import numpy as np
import random
import time
from keras.models import load_model
from pydantic import validate_arguments


class RPS_game():

    """This class contains all the necessary methods for
    playing the Rock, Paper, Scissors game"""


    def __init__(self):

        """See help(RPS_game) for all the details"""

        #self.model = load_model('keras_model.h5')
        #self.cap = cv2.VideoCapture(0)
        self.options = ['Rock', "Paper", "Scissors", "Lizard", "Spock", "Nothing"]
        self.points_computer = 0
        self.points_user = 0
        self.rounds_played = 0
    
    
    @staticmethod
    @validate_arguments
    def game_instructions():

        """This method displays the instructions of the game"""

        print(
            '''Welcome to an interactive version of Rock Paper Scissors! 
            When your camera will turn on, you will see the instructions on the screen.
            Show your choice after the GO! cue.
            ENJOY!
            '''
        )

    
    def start_video(self):
        
        """This method opens the user camera, displays instructions for running &
        stopping the game and starts acquiring frames"""

        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        ret, frame = self.cap.read()
        #crops camera to dimensions similar to ML model training
        cropped_frame = frame[200:1000, 300:1100]
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'Hold s to start countdown', (0, 100), font, 2, (118, 237, 250), 2, cv2.LINE_AA)
        cv2.putText(frame, 'Hold q to stop game', (800, 700), font, 2, (78, 99, 235), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

    
    def stop_video(self):

        """This methods stops the user camera and closes window"""

        self.cap.release()
        if self.rounds_played == 5:
            print(f'You played 5 rounds, the game is finished.')
        else:
            print(f'You left game before the outcome was determined')
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)


    def get_prediction(self) -> int:

        """This method searches for the highest prediction out of
        the four possible categories
        
        Returns
        -------
        int
            an integer represinting the index at which we can find the highest prediction number"""

        predictions = self.model.predict(self.data)
        idx = np.argmax(predictions[0])
        return idx


    def get_user_choice(self):

        """This method gets the user and computer choices
        and prints them out"""
        idx = self.get_prediction()

        if idx == 6:
            self.user_choice = 'None'
        else:
            self.user_choice = self.options[idx]
            print(f'You chose {self.user_choice}')
            #print(f'The computer chose {computer_choice}')


    def get_winner(self, user_choice):

        """This method decides the winner"""

        self.computer_choice = random.choice(self.options)
         
        if self.computer_choice == 'Rock' and user_choice == 'Scissors':
            self.winner = 'the computer'
            self.points_computer += 1
            self.rounds_played += 1

        elif self.computer_choice == 'Scissors' and user_choice == 'Paper':
            self.winner = 'the computer'
            self.points_computer += 1
            self.rounds_played += 1

        elif self.computer_choice == 'Paper' and user_choice == 'Rock':
            self.winner = 'the computer'
            self.points_computer += 1
            self.rounds_played += 1

        elif self.computer_choice == user_choice:
            self.winner = 'Nobody won this round!' 
            self.rounds_played += 1

        else:
            self.winner = 'you'
            self.points_user += 1
            self.rounds_played += 1


    def print_round_winner(self):

        """This method prints out each round's winner"""
        
        if self.winner == 'you' or self.winner == 'the computer':
            print(f'Round {self.rounds_played}: The winner of this round is {self.winner}\n') 
        elif self.winner == 'Nobody won this round!':
            print(f'Round {self.rounds_played}: {self.winner}\n')


    def get_game_outcome(self):

        """This method determines the game outcome"""

        if self.points_computer > self.points_user :
            print("You lost, the computer won :(")

        elif self.points_user > self.points_computer:
            print("You won! Go celebrate")
            

    def play_game(self):
        
        """This method integrates previous methods to play the RPS game"""

        self.game_instructions()

        while True:

            #initialises timer for countdown
            timer = 3
            self.start_video()

            #if user press s countdown starts
            if cv2.waitKey(80) & 0xFF == ord('s'):

                #returns time at the start of countdown
                prev = time.time()

                # if timer > 0 -timer is displayed on screen 
                while timer > 0:
                    font = cv2.FONT_HERSHEY_TRIPLEX
                    ret, frame = self.cap.read()
                    cropped_frame = frame[200 : 1000, 300 : 1100]
                    cv2.putText(frame, str(timer), (200, 250), font, 5, (255, 145, 0), 4, cv2.LINE_AA)
                    cv2.imshow('frame', frame)
                    cv2.waitKey(1)
                    cur = time.time()
                    
                    # decrease timer by 1 second
                    if cur - prev >= 1:
                        prev = cur
                        timer = timer - 1

                # when timer reaches 0, display GO! cue on the screen
                else:
                    ret, frame = self.cap.read()
                    cropped_frame = frame[200 : 1000, 300 : 1100]
                    font = cv2.FONT_HERSHEY_TRIPLEX
                    cv2.putText(frame, 'GO!', (200, 250), font, 5, (255, 145, 0), 4, cv2.LINE_AA)
                    cv2.imshow('frame', frame)
                    cv2.waitKey(30)

                    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                    image_np = np.array(resized_frame)
                    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                    self.data[0] = normalized_image
                    
                    #calls class methods to extract desired information about game outcome
                    user_choice = self.get_user_choice()
                    self.get_winner(user_choice)

                    #after playing 5 rounds outcome is displayed
                    if self.rounds_played == 5:

                        self.get_game_outcome()
                        self.stop_video()
                        break
                
            #if user press q camera and game stops
            elif cv2.waitKey(80) & 0xFF == ord('q'):
                
                self.stop_video()
                break    
        
            #reinitialise timer back to 3s - to prepare for another round
            else:
                timer = int(3)


if __name__ == '__main__':

    game = RPS_game()
    #game.play_game()