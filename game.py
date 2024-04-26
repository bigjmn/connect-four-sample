import random
def create_wingroups(b_width, b_height):
    all_wingroups = []
    #verticals 
    for i in range(b_width):
        for j in range(b_height-3):
            wingroup = []
            for k in range(4):
                wingroup.append((i, j+k))
            all_wingroups.append(wingroup)

    #horizontals
    for i in range(b_width-3):
        for j in range(b_height):
            wingroup = []
            for k in range(4):
                wingroup.append((i+k, j))

            all_wingroups.append(wingroup)

    #upward diags
    for i in range(b_width-3):
        for j in range(b_height-3):
            wingroup = []
            for k in range(4):
                wingroup.append((i+k, j+k))
            all_wingroups.append(wingroup)

    #downward diags 
    for i in range(b_width-3):
        for j in range(b_height-1, b_height-4, -1):
            wingroup = []
            for k in range(4):
                wingroup.append((i+k, j-k))
            all_wingroups.append(wingroup)
    return all_wingroups

class Board:
    def __init__(self, board_width=7, board_height=6):
        self.board_width = board_width 
        self.board_height = board_height
        self.board_state = [[" "]*board_height for i in range(board_width)]
    
    def set_dimensions(self, xdim, ydim):
        if xdim < 4 or ydim < 4:
            print("don't be a dick")
            return 
        
        self.board_width = xdim 
        self.board_height = ydim 
        # gotta resit so the state has these new dimensions 
        self.reset_game()

    @property
    def wingroups(self):
        return create_wingroups(self.board_width, self.board_height)
    
    def get_square(self, coords):
        (x_cord, y_cord) = coords 
        return self.board_state[x_cord][y_cord]
    
    def get_col_length(self, x_cord):
        col = self.board_state[x_cord]
        filled_spaces = 0
        for i in range(self.board_height-1, -1, -1):
            if col[i] != " ": filled_spaces +=1 
        return filled_spaces 
    def legal_choices(self):
        legals = []
        for i in range(self.board_width):
            if self.get_col_length(i) < self.board_height:
                legals.append(i)
        return legals 
    
    def check_win(self):
        for wg in self.wingroups:
            wg_marks = list(map(lambda x: self.get_square(x), wg))
            if wg_marks == ["R"]*4: return "R"
            if wg_marks == ["Y"]*4: return "Y"
        return None
    
    def place_piece(self, x_cord, mark):
        col_length = self.get_col_length(x_cord)
        if col_length >= self.board_height:
            print("that col is full")
        else:
            self.board_state[x_cord][col_length] = mark
            next_mark = "Y" if mark == "R" else "R"
            winner = self.check_win()
            return winner, next_mark 
        
    def reset_game(self):
        self.board_state = [[" "]*self.board_height for i in range(self.board_width)]

    def show_board(self):
        print()
        for row in range(self.board_height-1, -1, -1):
            rowstring = ""
            for i in range(self.board_width):
                rowstring += f"|{self.get_square((i, row))}"
            print(rowstring)

class Game:
    def __init__(self):
        self.board = Board()
        self.mark_to_play = "R"
        self.winner = None 

    def game_intro(self):
        chosen_w = None
        chosen_h = None
        while chosen_w == None:
            bw = input("Pick a board width (7): ")
            try:
                if bw == "": chosen_w = 7
                elif int(bw) < 4:
                    print("try something bigger than 4 bud")
                else: chosen_w = int(bw)
            except:
                print("not a valid width")

        while chosen_h == None:
            bh = input("Pick a board height (6): ")
            try:
                if bh == "": chosen_h = 6
                elif int(bh) < 4:
                    print("try something bigger than 4 bud")
                else: chosen_h = int(bh)
            except:
                print("not a valid width")

        return chosen_w, chosen_h

    def play(self):
        chosen_width, chosen_height = self.game_intro()
        self.board.set_dimensions(chosen_width, chosen_height)
        while self.winner == None:
            chosen_col = None
            if len(self.board.legal_choices()) == 0:
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
                

                
                 


    


    