# Story game



                                                          SPACE ADVENTURE: BACK HOME

                                                       A Python based adventure style game








                                                               December 17, 2020

                                                            University of St. Gallen

                                                      Skills: Programming – Introduction Level













                                                            Authors:						Student ID:


                                                           Jan Luckmann						19-607-688

                                                           Jean Delclos						19-618-990

                                                           Jérémy Huber						19-617-208

                                                           Justin Koren						18-613-364

                                                           Luca Erdmann						19-609-890





PROJECT DESCRIPTION

The project was created using Python and requires the user to import Pygame libraries for it to properly function. The game structure can be divided in two components: a general matrix of basic instructions that constitute the fundamental storyline and three advanced minigames that will challenge the player at different stages of the adventure. The core of the game is predominantly composed by while loops with if/ elif/ else statements. This allow for the player to choose different possible paths within the game and discover what the consequences of his or her choices will be. Given the limited scope of the game it was necessary to restrict the set of admissible answers and this fundamental function is covered by the else statement which will restart the loop whenever an inadmissible input is fed to the program. The individual minigames contained within the matrix are much more complex and constitute a truly interactive experience for the player. They are supported by Pygame and will be more thoroughly explained below in an individual manner. While the minigames’ codes have been derived from pre-existing online sources the main challenge in this project was to customize these well-known programs so that they would fit in our project and properly fulfill the function for which they were included. Each minigame begins or ends whenever a specific set of actions have been taken by the player. This was achieved by transforming each game in a function that could then be incorporated in the overall project.

The first mini game which comes up is the snake-game. 
The snake-game is an improved and adjusted version of the code from “wynanda1004” (https://gist.github.com/wynand1004/ec105fd2f457b10d971c09586ec44900). The player starts the ‘Main game loop’ by pressing one of the move-buttons (W, A, S & D). As like any other snake-game, once the “head” (black square) reaches the “food” (red circle), the snake grows one block of tail (grey square). Each time the snake eats one unit of food the score increases by one and the game-speed increases. If the score is less than 5 and the snake crashes into the wall or itself, the game resets. It the score is 5 or higher the main loop breaks after the player crashes into the wall. Afterwards the the player has passed the game. The game then continues in the main frame

After the player found the right pill and turned back into a person. The second mini game is bounce is started. It is an adjusted version of the code from “georgecoopers” (https://github.com/georgecoopers/Pygame-Progression/tree/master/Jump!). The player first sees the info-screen, which describes the game and then starts the game by pressing a key on the keyboard. Afterwards the game starts. The controls are through the keys: A to go left and D to go right and space to jump. As soon as, the player reaches 20 points the game loop of the bounce game is interrupted, and the main loop continues. If the player crashes before he reaches the top of the rocket the game is restarted. 


After the player managed to escape with the rocket, he runs into a meteor-shower. The goal is to evade or shoot down the meteors to escape and win the game. The game was built using the pygame module and pictures from flaticon.com. The game can be run separately but is also implemented in our main game as the last stage. 




The basic of the code is based on the youtuber: “buillditwithpython” (https://www.youtube.com/playlist?list=PLhTjy8cBISEo3SzET7Fc3-b4miKWp41yX). But was adjusted to better fit the storyline of the main game. Instead of a “space-invader” game it is now a “meteor- evasion” game.

The commands are “a” for left, “w” for up, “d” for right, “s” for down and SPACE to shoot.

For the program to run correctly it is crucial to have the pictures in the current working directory of the Python file. Otherwise the specified path will not lead to the pictures and the game will run an error. Normally this is automatically so when downloading the folder from Github. In case this should not work, please add them to the correct working directory.



Attribution to the creators of the images according to the rules of flaticon.com
Bullet:
&lt;div&gt;Icons made by &lt;a href=&quot;https://www.flaticon.com/authors/smashicons&quot;
title=&quot;Smashicons&quot;&gt;Smashicons&lt;/a&gt; from &lt;a href=&quot;https://www.flaticon.com/&quot;
title=&quot;Flaticon&quot;&gt;www.flaticon.com&lt;/a&gt;&lt;/div&gt;
Spaceship:

&lt;div&gt;Icons made by &lt;a href=&quot;https://www.flaticon.com/authors/freepik&quot;
title=&quot;Freepik&quot;&gt;Freepik&lt;/a&gt; from &lt;a href=&quot;https://www.flaticon.com/&quot;
title=&quot;Flaticon&quot;&gt;www.flaticon.com&lt;/a&gt;&lt;/div&gt;

Meteor:
&lt;div&gt;Icons made by &lt;a href=&quot;https://www.flaticon.com/authors/pixel-perfect&quot; title=&quot;Pixel
perfect&quot;&gt;Pixel perfect&lt;/a&gt; from &lt;a href=&quot;https://www.flaticon.com/&quot;
title=&quot;Flaticon&quot;&gt;www.flaticon.com&lt;/a&gt;&lt;/div&gt;






