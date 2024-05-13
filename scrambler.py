import cube
import random 

legal_moves = "U U2 U' D D2 D' F F2 F' B B2 B' R R2 R' L L2 L'".split()

class Scrambler():
    def __init__(self, leg=legal_moves):
        self.legal_moves = leg

    def generate_scramble(self, seed=None):
        if seed < 0 or seed > 1000:
            raise Exception("seed should be 0-1000")
        random.seed(seed)
        scramble = []
        while len(scramble) < 20:
            move = random.choice(self.legal_moves) 
            if len(scramble) >= 1 and move[0] == scramble[-1][0]:
                continue
            scramble.append(move)
        return " ".join(scramble)
