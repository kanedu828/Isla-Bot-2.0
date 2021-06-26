# Isla-Bot-2.0

## Overview

Isla Bot 2.0 takes its focus on the mining game. In this revamp, many more additions and mechanics were added to the mining game to give it more depth. 
The bot is current in its beta state.

## Commands

`;mine` Mine in the current cave you are in.\
`;cave` List all of your available caves.\
`;cave <cave name>` Switch to the specified cave.\
`;stats` View your stats. i.e Your level, total exp, gold, and mining stats.\
`;equip <equipment name>` Equip your specified equipment.\
`;gear` View all of your equipped equipment.\
`;gear <equipment name>` Display in detail your specified equipment.\
`;inventory` List your inventory.\
`;leaderboard` View the leaderboard based off of total exp.\
`;bonus <equipment name>` Add bonuses to your specified equipment.\

## Mining
By using the `;mine` command, you mine your cave in the chance to recieve gold, equipment, or exp. Each cave drops different loot and has different odds to drop loot.

## Caves
Each cave has a level requirement that is needed for someone to enter it. Every cave drops a set amount of exp. For example, the Beginner cave drops 1 exp per mine while the Dark Cave drops 10 exp per mine.\
Cave loot is seperated into 5 categories: Nothing, Common, Rare, Epic, Legendary\
Typically, the latter categories will have a lower chance to drop.\
Additionally, some caves can only be mined a certain amount. For example, if a cave only has 1,000 mines, it can no longer be mined when it is mined a total of 1000 times by all miners. The remaining mines in a cave gets reset periodically. Some caves, however, can be mined an infinite amount of times.\
If you're interested in viewing all available caves, you can find them [here](https://github.com/kanedu828/Isla-Bot-2.0/blob/master/data/caves.py).
If you understand the cave list in that file and you would like to help out, feel free to list the caves in a readable format here with a pull request!

## Stats
Current there are four different stats for a user: power, speed, exp, luck\
Power: You get x amount of extra gold each time you mine gold.\
Speed: Cooldown for mining reduced by speed / 100. (This stat will most likely be nerfed)\
Exp: You get x amount of extra exp each time you mine exp.\
Luck: Your chances of recieving Epic or Legendary loot is increased by luck / 10,000.\
Your stats can be added raw (+) or added as a percentage (%).\
For example, if you have power + 6, you will get 6 power to your total power stat. If you have ower 6%, you will get an additional 6% of your total power added to your total power.
