# Testare Sisteme Software - Python Unit Testing

### Rubick Cube Scrambler and Solver

## Introduction

For our project we created a minimalistic text-based app, which manages to create move sequences for scrambling the Rubick's Cube, but also solves them.

The Rubick's Cube is a toy which consists of a regular cube with each face painted in a different color. Each of the 6 faces of the cube can move laterally, scrambling each of the 9 squares of a face. The purpose of the game is to move the faces of a scrambled cube in such a way that the initial 6 colors are restitued, thus solving the cube.

Our app gives the user the option of generating such a scramble, of precisely 20 moves. Such a scramble, for example would be "F' B' L2 U R' F2 U2 D' B' L F2 R L' D F2 U F R2 F' D'", where each letter indicates which face should be moved and in which direction. (F' for example indicates that the Front face should be moved counter-clockwise)

Such a scramble can then be solved by our app, giving the combination of moves (not unique), that can be applied to revert the cube to the initial configuration. The solution for the scramble mentioned before is "U R U2 B' U2 L F2 D B U' D2 B U' R2 B2 U' R2 U2 F2 L2 D2 F2". We invite the reader to verify on their own cube.

## Running the app

The app can be run by simply typing "python3 main.py" in the terminal.


## Running the tests

3 types of tests have been implemented:

- Unit Tests for the cube.py module, which stores the cube in memory, which can be run by typing "python3 -m unittest test_cube.py" in the terminal.

- Functional and Structural tests for the main.py (hosts the main app and text-based interface) and scrambler.py (stores the scramble generator) modules, which can be run by typing "python3 -m unittest test_main_scrambler.py" in the terminal.

- Mutant Testing, for the same 2 modules as before, which can be run by typing "mut.py --target main.py --unit-test test_main_scrambler.py" in the terminal.

## Documentation

Kindly note that a thorough documentation in Romanian has been created for the purpose of grading this project, and I'd humbly invite you to assess it's contents, in the "Documentatie_A_8_Tudose_Radu.pdf" file in this repository. 


Below are installation details for further development.

## HOW TO INSTALL:

# LINUX
- install python3
- make a virtual enviroment using: ```python3 -m venv env```
- activate the env: ```source env/bin/activate```
- now install the packages that we use: ```pip install -r requirements.txt```
- and you can work

# WINDOWS
- install python
- make a virtual enviroment using: ```python -m venv env```
- activate the env: ```env\Scripts\activate```
- now install the packages that we use: ```pip install -r requirements.txt```
- and you can work

## WORK FLOW:
- pull all the changes from git
- activate the env
- if requirements.txt is modified update the packages by installing the requirements
- if you need to install a package: ```pip install package_name```
- to update the requirements file with the new packages: ```pip freeze > requirements.txt```
- to deactivate (leave the env): ```deactivate```
- when working always be in the env, deactivate when you're done

## TO DO:
- to implement CFOP variation of the solver
- make a scanner for the cube using the camera
- make a layout for the application
- make tests using a library