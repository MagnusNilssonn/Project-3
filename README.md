# Battleships

The goal of this project was to test my knowledge and understanding of python coding, I decided quite early on to try a simpler game and the choice fell on battleships, a game that I always appreciated.


## Lucidchart 

- I started to make a Lucidchart to map the workflow for the game.



![Mall Lucidchart](https://i.postimg.cc/6qnwmD4J/Battleships.jpg)

# Technologies Used:

## Programming Languages:

- Python

## Gitpod

- I used gitpod to write the code

## Github

- GitHub is used to store the projects code after being pushed from Gitpod 

<br><br>
# The Game

- When you start the game you will come to the game field and a welcome message, "You have 15 attempts to find the 2 ships".
You start by choosing row 1-7.
- If you do not select a valid row. It prints :Row must be a number between 1 and 7.


<br><br>
![Landing Page](https://i.postimg.cc/j5jGpCCr/landing.png)


- If u miss a "miss" message will be printed and the turns countdown by 1.

![Miss](https://i.postimg.cc/g27fRG0z/miss.png)

- If u hit a "hit" message will be printed and the turns countdown by 1.

![Hit](https://i.postimg.cc/YqvcS4pn/hit.png)

- If u dont find the ships in 15 turns a "game over" message will be printed

![Game over](https://i.postimg.cc/T38RMjrq/gameover.png)

- If u manage to find both ships in 15 turns a "congratulations" message will apear

![WellDone](https://i.postimg.cc/VkMXmF2Y/welldone.png)

# Testing 

- When I started testing everything worked fine until I typed "Enter" instead of a number or letter and the program crashed which caused me to retype one of the functions. Now it works as I want.
- I installed autopep8 and let it run alongside
- I've tested every possible error I can think of and also ran the code at https://pep8ci.herokuapp.com/ with no error to report.


# Things to implement in the future

- The option for players to choose diffrent gridsize.
- Multiplayer option if it´s 2 human players who wants to play.


 # Deployment
 ## Heroku
 ### This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com 
2. Create a new app, add app name and your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars, add your sensitive data
6. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
7. Enter your repository name and click on it when it shows below
8. Choose the branch you want to buid your app from
9. If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository




The live link can be found here - https://battleship--pp3.herokuapp.com/


# Credits 

- My mentor Naoise Gaffney for valuable tips and reflections, not least in the bug search
- Code Institute - For the course material and the support throughout.
- Knowledge Mavens for really good tips on the game code: https://www.youtube.com/@KnowledgeMavens
- ArjanCodes for tips on how to clean up the code: https://www.youtube.com/@ArjanCodes
- Lucidchart: https://www.lucidchart.com/
- The readme content "how to deploy to Heroku" was borrowed from https://github.com/johnvenkiah/CI_PP3_John_Venkiah#readme