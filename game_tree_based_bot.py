from overflow import overflow
from data_structures import Queue

def copy_board(board):
    """
        This function makes a deep copy of the board.

        Parameters:
            board(list): the table storing the current board.

        Returns:
            list: a deep copy of the current board.
    """
    current_board = []
    height = len(board)
    for i in range(height):
        current_board.append(board[i].copy())
    return current_board

def evaluate_board (board, player):
    """
        This function for evaluating leaf nodes, it returns the score for the player.
        There are three states for the board, winning, non-winning(non-losing) and losing.

        Parameters:
			board(list): The table need to be evaluated.
            player(int): The player this function evaluated for.
        
        Returns:
            +∞: If it is a winning board, return +∞.
            -∞: If it is a losing board, return -∞.
            int: If is a non-winning board, return the score calculated.
    """
    score = 0
    winning_board = losing_board = True
    # go through every cell on the board, count the score
    for row in board:
        for num_of_gem in row:
            # check the if the player is winning or losing
            if winning_board or losing_board:
                if num_of_gem * player > 0:
                    # if the player has any gems on the borad, it is not in losing state
                    losing_board = False
                elif num_of_gem * player < 0:
                    # if the opponent player has any gems on the board, it is not in winning state
                    winning_board = False
            score += (num_of_gem * player)

    # check if player is winning or losing, otherwise return the score
    if winning_board:
        return float('inf')
    if losing_board:
        return float('-inf')
    return score

class GameTree:
    """
        The class for a game tree. 
        While a GameTree is being created, it will generate possible moves for the game board.
        The GameTree does not contain all the possible moves, the branches that a player will never take have been cut off during the creation period by the idea of alpha-beta pruning.
        The minimax algorithm is applied in this class to determine the score for a node in the game tree.
    """
    class Node:
        """
            The class for a node.
            It is used to store informations for a move(action) in the game.
        """
        def __init__(self, board, depth, player, tree_height = 4):
            """
                Initialize a node for the GameTree.

                Parameters:
                    board(list): the table storing the current board.
                    depth(int): a number indicating the node is in which level of the tree.
                    player(int): 1 or -1 that indicating the node is for which player.
                    tree_hight(int, optional): the height limitation of the tree, default to 3.
                
                Returns:
                    None
            """
            self.board = board
            self.depth = depth
            self.player = player
            self.tree_height = tree_height
            self.possible_moves = []
            self.children = []
            self.score = 0

    def __init__(self, board, player, tree_height = 3):
        """
            Initialize a GameTree object.
            The player who passed into this function will be the maximazing player.
            The GameTree will generate the best move for this player.

            Parameters:
                board(list): the table storing the current board.
                player(int): 1 or -1 that indicating the GameTree object is for which player, in another word, the player will be the maximazing player in this game.
                tree_hight(int, optional): the height limitation of the tree, default to 3.
   
            Returns:
                None
        """
        self.player = player
        self.board = copy_board(board)
        self.root = self.Node(self.board, 0, self.player, tree_height)
        self.build_tree(self.root, float('-inf'), float('inf'), True)

    def check_board_state(self, board, player):
        """
            This function is for checking if the board is in a terminal state, which are winning and losing state.
            Three states concluded:
                - Winning state, the player is winning.
                - Losing state, the player is losing.
                - Continuing state, there is no winner yet, game can be continued.

            Parameters:
                board(list): the table storing the current board.
                player(int): 1 or -1 that indicating the maximizing player in this game.

            Returns:
                1: indicate the current board is in a terminal_state, which is winning_state
               -1: indicate the current board is in a terminal_state, which is losing_state
                0: indicate the current board is in continuing_state
        """
        # default to ternimal_state, check every cell in the board
        winning_board = losing_board = True
        for row in board:
            for col in row:
                if not winning_board and not losing_board:
                    return 0
                if col * player > 0:
                    # if any gem belongs to the player, the player is not losing
                    losing_board = False
                elif col * player < 0:
                    # if any gem belongs to the opponent, the player is not winning
                    winning_board = False
        if not winning_board and not losing_board:
            return 0
        elif winning_board:
            return 1
        elif losing_board:
            return -1
        
    def generate_possible_moves(self, board, player):
        """
            This function generate all the possible moves for the player based on given board.

            Parameters:
                board(list): the table storing the current board.
                player(int): 1 or -1 that indicating the player who is going to take a move.

            Returns:
                list: a list of all the possible moves, each move is a tuple of (row, col).

        """
        possible_moves = []
        # only generate for board in continuing_state(0)
        if self.check_board_state(board, player) == 0:
        # generate all possible moves for the board in passed-in node
            for row in range(len(board)):
                for col in range(len(board[row])):
                    # record possible moves, a piece can be placed at a cell 
                    # which is empty or already occupied by the player
                    if board[row][col] == 0 or board[row][col] * player > 0:
                        possible_moves.append((row, col))
        return possible_moves

    def build_tree(self, node, alpha, beta, is_maximizing_player):
        """
            This function build the game tree.
            It is applying minmax algorithm to calculate the score for inner nodes. 
            While scoring a inner node, it offers:
                - The maximum score for the player(the maximizing_player) to chose
                - The minimum score for the opponent to chose.
            It is applying alpha-beta pruning to be more efficient. The game tree will cut off the branches never be chosen.

            Parameters:
                node(Node): the root node to start to create a game tree.
                alpha(float): the highest score the player can take, -inf is passed in initially.
                beta(float): the lowest score the player will accept from the opponent, inf is passed in initially.
                is_maximizing_player(boolean): to indicate if this function is for the player, True is passed in initially.
            
            Returns:
                float: inf or -inf will be returned if is the game has a winner.
                int: the score that represents the highest score for the player's node and the lowest score for the opponent's node.
        """
        # if the board is in a terminal_state(1 or -1) or depth reached the maximum height, evaluate the board
        if self.check_board_state(node.board, node.player) or node.depth == node.tree_height - 1:
            node.score = evaluate_board(node.board, node.player)
            return node.score
        
        # player switching start from depth 2, player for depth 1 is same as root node
        if node.depth == 0:
            player = node.player
        else:
            player = -node.player

        node.possible_moves = self.generate_possible_moves(node.board, player)
        # if the board is in a continuing_state, build subtree for possible moves of the board
        if is_maximizing_player:
            best_score = float('-inf')
            # create children nodes for each possible move
            for move in node.possible_moves:
                # place the piece into a new board
                new_board = copy_board(node.board)
                row, col = move
                new_board[row][col] += player
                # do overflow if needed
                overflow(new_board, Queue())
                # create a child node, and store it into the parent's node list
                child_node = self.Node(new_board, node.depth + 1, player)
                node.children.append(child_node)
                # build subtrees recursively until meet the maximum height or reach a leaf
                # the opponent takes the next turn(level of the tree), record the socre result
                score_result_from_next_level = self.build_tree(child_node, alpha, beta, False)
                # update the best score the maximizing_player can take from the opponent's moves
                best_score = max(best_score, score_result_from_next_level)
                # update the best score(alpha) the maximizing_player can take on the current subtree
                alpha = max(alpha, score_result_from_next_level)
                # if the score offered by opponent(beta) is not greater than the score the maximizing_player can take(alpha)
                # stop exploring more possible moves, the maximizing_player will not choose this subtree
                if beta <= alpha:
                    break
            node.score = best_score
            return best_score
        else:
            worst_score = float('inf')
            for move in node.possible_moves:
                # place the piece into a new board
                new_board = copy_board(node.board)
                row, col = move
                new_board[row][col] += player
                overflow(new_board, Queue())
                # create a child node, and store it into the parent's node list
                child_node = self.Node(new_board, node.depth + 1, player)
                # get the score result from next level(the the maximizing_player's choice)
                score_from_next_level = self.build_tree(child_node, alpha, beta, True)
                # update the worst_score to the lowest from current possible moves
                worst_score = min(worst_score, score_from_next_level)
                # update the worst score for the maximizing_player on the current subtree
                beta = min(beta, score_from_next_level)
                if beta <= alpha:
                    break
            node.score = worst_score
            return worst_score

    # this function is a pure stub.  It is here to ensure the game runs.  Once you complete
    # the GameTree, you will use it to determine what to return.
    def get_move(self):
        """
            This function find the best move for the current board.

            Parameters:
                None
            
            Returns:
                tuple: a (row, col) that indicate the best move.
        """
        best_score = float('-inf')
        score_index = None

        for i in range(len(self.root.children)):
            if self.root.children[i].score == float('inf'):
                return self.root.possible_moves[i]
            if self.root.children[i].score > best_score:
                best_score = self.root.children[i].score
                score_index = i
        return self.root.possible_moves[score_index]

    def clear_tree(self):
        """
            This function destroy the GameTree object.
            It destroy the game tree in post-order.

            Parameters:
                None

            Returns:
                None
        """
        def clear_tree_recursively(subtree):
            # if subtree is not empty, keep removing the last child node from the list
            while subtree.children:
                child = subtree.children.pop()
                clear_tree_recursively(child)
        clear_tree_recursively(self.root)
