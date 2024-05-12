import cube
import random 

legal_moves = "U U2 U' D D2 D' F F2 F' B B2 B' R R2 R' L L2 L'".split()

class Scrambler():
    def __init__(self, leg=legal_moves):
        self.legal_moves = leg

    def generate_scramble(self, seed=None):
        if seed is None:
            raise Exception("seed can't be non Null")
        if seed < 0 or seed > 9:
            raise Exception("seed should be a positive digit")
        
        if seed % 2 == 0:
            for move in ["U", "U'", "U2"]:
                self.legal_moves.remove(move)

        random.seed(seed)
        scramble = []
        while len(scramble) < 20:
            move = random.choice(self.legal_moves)
            if len(scramble) >= 1 and move[0] == scramble[-1][0]:
                continue
            scramble.append(move)
        self.legal_moves.extend(["U", "U'", "U2"])

        return " ".join(scramble)
