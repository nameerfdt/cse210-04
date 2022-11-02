# Greed Overview
___
Greed is a game in which the player, a miner, seeks to gather as many falling gems as possible.
As the miner moves side to side and mines a gem, a point is earned. If a boulder is mined, the 
player loses a point. Gems and boulders are removed when either touched or untouched. The game
ends when the miner closes the mine, aka the game window. 

## Getting Started
___

Make sure you have Python 3.10 or newer installed and running on your machine. Open a terminal and 
browse to the project's root folder. Start the program by running the following command.
```
__main__.py
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the puzzle folder and click the "run" button.

## Project Structure
___

__main__

## Services

### Keyboard Service

* Acts as an interface to check what keyboard keys are being held by the user. 

### Video Service

* Sets window bounds and visual output to user.

## Shared

### Color

* Defines and stores a color for an object, recieves an RGB input.

### Point

* X and Y coordinate storage for an object.

## Casting

### Actor

* A component of the game that stores properties relating to itself. It acts as an individual component of the game.

### Artifact

* A subset of Actor that moves downward on the screen different from the player actor. Is a subset of two groups, boulders and gems.

### Cast

* Storage for individual artifacts and actors to exist. Moves Artifacts and Actors relevant to their velocity. Applies mainly to miner and arifacts.

## Directing

### Director

* Operates the gameplay and loops until user is bored.

## Required Technologies
---
* Python 3.10
* Raylib Python 4.2

## Authors
---
* Alex Dahl (alexdahl@byui.edu)
* Tracy Freeman (nameerfdt@byui.edu)
* Joshua Herman (her21095@byui.edu)
