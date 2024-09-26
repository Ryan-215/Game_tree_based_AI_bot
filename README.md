# Game Tree Based AI Bot for 2D Board Game
I developed an AI bot that plays a 2D board game using game tree algorithms, evaluation functions, and alpha-beta pruning, enhancing the bot's strategic decision-making through look-ahead capabilities. This project involved implementing a game tree structure to analyze potential moves and counter-moves, allowing the bot to make optimal decisions based on various game scenarios.

## Game Mechanics  
The AI bot operates within a unique 2D board game environment where players strategically place gems to control the board. Each turn, gems are added to empty squares or squares already occupied by the player’s gems. A gem overflow mechanism spreads gems to neighboring squares, altering the game’s state dynamically. The game ends when all gems on the board are the same color, signifying a win for that player.  

## Key Features
### Custom Overflow Rule  
I implemented the game's overflow mechanics, where gems spread to neighboring cells when reaching a certain threshold. This implementation was done from scratch, adding complexity and strategic depth to the game as players must manage gem placement carefully to maximize their advantage.  

### Data Structure Implementations  
As part of my approach, I also implemented Queue, Stack, and Deque data structures to practice and enhance the project’s efficiency. These structures were utilized for various aspects of the game logic, including managing moves and simulating game states, allowing for organized and efficient processing of game data.

### Evaluation Function  
I designed and implemented an evaluation function to score the board state from a given player’s perspective. The function assigns scores based on board conditions, ensuring that winning scenarios score higher than non-winning ones, and losing scenarios score lower than non-losing ones. The evaluation accounts for gem placement, overflow mechanics, and player advantage.  

### Game Tree Implementation  
I constructed a game tree data structure, which models the potential moves of both the AI and its opponent. The tree’s nodes represent different board states, branching out to simulate future moves. The tree is generated up to a set height, where each node evaluates the board state using my custom evaluation function.  

### Minimax Algorithm with Alpha-Beta Pruning  
To determine the optimal move, I integrated a minimax algorithm enhanced with alpha-beta pruning into the game tree. The minimax algorithm recursively evaluates each node, scoring them based on whether the AI or the opponent is making the move. Alpha-beta pruning was used to eliminate unnecessary branches of the tree, significantly improving computational efficiency by reducing the number of nodes evaluated. This approach allows for deeper exploration within the same computational limits, resulting in more strategic and informed gameplay.