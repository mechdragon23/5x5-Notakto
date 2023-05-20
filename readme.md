# Final Project
CPSC481-01: Artificial Intelligence

DUE: 19 May 2023 

## Group Members

- **Chandra Lindy** - chandra.lindy@csu.fullerton.edu
- **Alexander Au** - aau6@csu.fullerton.edu
- **Dilhan Franco** - dilhanfranco@csu.fullerton.edu
- **Frank Salgado-Gonzalez** - franksalgado@csu.fullerton.edu
  
## Project Overview
Notakto is a variant of the classic game of tic tac toe that differs in a fundamental way. Unlike traditional tic tac toe, where two players take turns placing their symbols (X or O) on a 3x3 grid, in Notakto, both players place the same symbol, say X; the first player to create 3 in a row of X's loses the game. 

## Technology Used
Python 3.11.0

# How to Execute
Clone the Repository into desired file directory
```
git clone https://github.com/mechdragon23/5x5-Notakto.git
```
Change directory to ```5x5-Notakto``` folder
```
cd ../5x5-Notakto
```
Install all necessary requirements to run app
```
pip freeze > requirements.txt
pip install -r requirements.txt
```
## Run app using User Interface 
In the UI version we defaulted to a 15x15 layout (NxN will be added in the future), and the user against our Hard AI
```
python notakto.py
```
Click ```Settings``` to change AI difficulty and layout (NxN) **UNDER DEVELOPMENT**

Click ```Quit``` to exit game

15x15 User vs. Hard AI
![notakto-ui](https://github.com/mechdragon23/5x5-Notakto/assets/53587310/0f97adb3-9246-4458-a51f-e903056af343)

## Run app in Terminal
In the Terminal version, the player can test the different difficulty level AI's against each other and layout is NxN. Follow instructions given at the bottom of ```project.py```
```
python project.py
```
NxN Hard AI vs. Medium AI (8x8 pictured), Hard AI wins 100% of the time
![notakto-terminal](https://github.com/mechdragon23/5x5-Notakto/assets/53587310/f69a9c91-4284-41f7-8eba-b7e69ab4a0db)


