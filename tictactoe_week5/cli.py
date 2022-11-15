#from logic import make_empty_board
import logic


if __name__ == '__main__':
    board = logic.make_empty_board()
    winner = None
    player = None
    if player == None:
        player_with_bot = input('Are you playing alone? Please enter Y or N')
        if player_with_bot == 'N':
            player = input('Please pick either X or O to play the game')
            print('Player 1, you are ', player)
            player_b = logic.other_player(player)
            print('Player 2, you are ', player_b)
            turn = player
            while winner == None:
                if logic.board_with_space(board) is False:
                    winner = 'Even'
                    print('This game ends in a draw')
                else:
                    print(turn, "TODO: take a turn!")
                    print('This is the current board', board)
                    player_row_choice = int(input('Please enter the row you want to change?'))
                    player_col_choice = int(input('Please enter the col you want to change?'))
                    if logic.empty_spot(board, player_row_choice, player_col_choice) is True:
                        logic.make_move(board, turn, player_row_choice, player_col_choice)
                        print('Here is the updated board: ', board)
                        if logic.get_winner(board) is not None:
                            winner = logic.get_winner(board)
                            print('Congratulations. ', winner, ' has won the game!')
                        else:
                            if turn == player:
                                turn = player_b
                            else:
                                turn = player
                    else:
                        print('Please re-enter your turn.')
        elif player_with_bot == 'Y':
            player = input('Please pick either X or O to play the game')
            print('Player 1, you are ', player)
            Bot = logic.bot(logic.other_player(player))
            player_b = Bot.name()
            turn = player
            while winner == None:
                if logic.board_with_space(board) is False:
                    winner = 'Even'
                    print('This game ends in a draw')
                else:
                    if turn == player:
                        print(turn, "TODO: take a turn!")
                        print('This is the current board', board)
                        player_row_choice = int(input('Please enter the row you want to change?'))
                        player_col_choice = int(input('Please enter the col you want to change?'))
                        if logic.empty_spot(board, player_row_choice, player_col_choice) is True:
                            logic.make_move(board, turn, player_row_choice, player_col_choice)
                            print('Here is the updated board: ', board)
                            if logic.get_winner(board) is not None:
                                winner = logic.get_winner(board)
                                print('Congratulations. ', winner, ' has won the game!')
                            else:
                                turn = player_b
                        else:
                            print('Please re-enter your turn')
                    elif turn == player_b:
                        logic.bot.move(board, player_b)
                        print('Here is the updated board: ', board)
                        if logic.get_winner(board) is not None:
                            winner = logic.get_winner(board)
                            print('Congratulations. ', winner, ' has won the game!')
                        else:
                            turn = player

        # TODO: Show the board to the user.
        # TODO: Input a move from the player.
        # TODO: Update the board.
        # TODO: Update who's turn it is.
