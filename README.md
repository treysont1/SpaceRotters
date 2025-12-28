## Space Rotters
## CS110 A0/B1 Final Project Fall 2025
## Team Members
## Stephen Limtom, John Schaetzle, Abdoul Razakou Mahaman Sani, Treyson Thelusma
***
## Project Description
## We made a recreation of classic games like Galaga and Space Invaders but added our own modern twist to make our game more approachable for younger audiences. We used brainrot characters as our enemies instead of aliens, modernizing the game.
***
## GUI Design
### Initial Design
![initial gui](assets/initial_design.jpg)
### Final Design
![final gui](assets/final_design.png)
## Program Design
### Features
1. Levels of increasing difficulty.
2. Player lives system (3 lives).
3. Sound effects.
4. Horizontal movement.
5. Point system.
### Additional Modules
1. pygame (used for visualizations and sprite mechanics)
2. random (used to generate random intergers for randomization of shot speed)
### Classes
- Player: Creates the ship that the player will be controlling to play the game, uss the fighter jet png.
- Player_Projectile: Creates the projectiles that are launched from the player.
- Enemies: Creates the enemy brainrot characters that the player has to defeat.
- Enemy_Projectile: Creates the projectiles that are launched from the player.
- Background: Creates and stores a sprite or image.
- Start: Creates a start button for the game.
- Replay: Creates a replay button for when the game ends.
- Exit: Creates a button to exit the game when the game ends.
- Brainrotters: Creates the titlecard for the game.
- Loser: Creates the losing message.
- Winner: Creates the winning message.
## ATP
Test Case 1: Player Movement
Test Description: Verify that the player's spaceship moves left and
right as expected.
| Step |Procedure |Expected Results |
| 1 | Run main program |GUI window appears with start screen
| 2 | click "Start" button | display changes to gamemode with instructions detailed
| 3 | click and hold left arrow | the player's spaceship should move left 
| 4 | click and hold right arrow | the player's spaceship should move right 

Test Case 2: Blaster Collision
Test Description: Verify that the player's shots from blaster eliminates enemies
| Step |Procedure |Expected Results |
| 1 | Start game |GUI window appears with start screen
| 2 | move under enemy and click spacebar | fire a player's bullet towards an enemy ship. 
| 3 | Verify that bullet hit enemy | enemy should disappear and score count should increase
| 4 | Fire a bullet and miss enemy ship | bullet should go past enemies 
| 5 | Verify that bullet did not hit enemy | enemy continues moving and score stays the same

Test Case 3: Level Progression
Test Description: Verify that the player upgrades and level of difficulty increases
| Step |Procedure |Expected Results |
| 1 | Start game |GUI window appears with start screen
| 2 | eliminate all enemies | all enemies disappear and more reappear 
| 3 | Click spacebar | player's number of shots fired per click should increase by 1

Test Case 4: Damage
Test Description: Verify that the player downgrades and loses lives
| Step |Procedure |Expected Results |
| 1 | Start game |GUI window appears with start screen
| 2 | Get hit by enemy attack/bullet | game should pause and resume, player loses points, and player explodes and returns to middle
| 3 | Click spacebar | player's number of shots fired per click should decrease by 1, unless first level

Test Case 5: Replay
Test Description: Verify that the user can play after losing or winning
| Step |Procedure |Expected Results |
| 1 | Start game |GUI window appears with start screen
| 2 | Play until end and eliminate all enemies | winner screen should appear with score
| 3 | Click "Play Again" button | game restarts and player score is set back to 0
| 4 | Get hit by enemies three times | loser screen should appear with score
| 5 | Click "Play Again" button | game restarts and player score is set back to 0



