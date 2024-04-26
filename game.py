import random
def create_wingroups():
    all_wingroups = []
    #verticals 
    for i in range(7):
        for j in range(3):
            wingroup = []
            for k in range(4):
                wingroup.append((i, j+k))
            all_wingroups.append(wingroup)

    #horizontals
    for i in range(4):
        for j in range(6):
            wingroup = []
            for k in range(4):
                wingroup.append((i+k, j))

            all_wingroups.append(wingroup)

    #upward diags
    for i in range(4):
        for j in range(3):
            wingroup = []
            for k in range(4):
                wingroup.append((i+k, j+k))
            all_wingroups.append(wingroup)

    #downward diags 
    for i in range(4):
        for j in range(5, 2, -1):
            wingroup = []
            for k in range(4):
                wingroup.append((i+k, j-k))
            all_wingroups.append(wingroup)
    return all_wingroups

class Board:
    def __init__(self):
        self.board_state = [[" "]*6 for i in range(7)]

    def get_square(self, coords):
        (x_cord, y_cord) = coords 
        return self.board_state[x_cord][y_cord]
    
    def get_col_length(self, x_cord):
        col = self.board_state[x_cord]
        filled_spaces = 0
        for i in range(5, -1, -1):
            if col[i] != " ": filled_spaces +=1 
        return filled_spaces 
    def legal_choices(self):
        legals = []
        for i in range(7):
            if self.get_col_length(i) < 6:
                legals.append(i)
        return legals 
    
    def check_win(self):
        for wg in create_wingroups():
            wg_marks = list(map(lambda x: self.get_square(x), wg))
            if wg_marks == ["R"]*4: return "R"
            if wg_marks == ["Y"]*4: return "Y"
        return None
    
    def place_piece(self, x_cord, mark):
        col_length = self.get_col_length(x_cord)
        if col_length >= 6:
            print("that col is full")
        else:
            self.board_state[x_cord][col_length] = mark
            next_mark = "Y" if mark == "R" else "R"
            winner = self.check_win()
            return winner, next_mark 
        
    def reset_game(self):
        self.board_state = [[" "]*6 for i in range(7)]

    def show_board(self):
        for row in range(5, -1, -1):
            rowstring = ""
            for i in range(7):
                rowstring += f"|{self.get_square((i, row))}"
            print(rowstring)

class Game:
    def __init__(self):
        self.board = Board()
        self.mark_to_play = "R"
        self.winner = None 

    def play(self):
        while self.winner == None:
            chosen_col = None
            if len(self.board.legal_choices) == 0:
                self.winner = "Tie"
                return
            #player chooses 
            if self.mark_to_play == "R":
                
                while chosen_col not in self.board.legal_choices():
                    chosen_col_str = (input("choose a column "))
                    chosen_col = int(chosen_col_str)

            #computer chooses 
            if self.mark_to_play == "Y":
                chosen_col = random.choice(self.board.legal_choices())

            winner, next_mark = self.board.place_piece(chosen_col, self.mark_to_play)
            self.winner = winner 
            self.mark_to_play = next_mark 
            self.board.show_board()

        self.board.reset_game()

new_game = Game()
new_game.play()
                

                
                 


    


    