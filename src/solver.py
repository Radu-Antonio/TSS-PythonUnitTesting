import kociemba
import cube 

class Solver():
    def solve_CFOP(self, scramble=""):
        c = cube.Cube()
        c.apply_moves(scramble)
        solution = []
        legal_moves = "U U2 U' D D2 D' F F2 F' B B2 B' R R2 R' L L2 L'".split()
        # cross
        # f2l 
        # oll
        # pll
        return " ".join(solution)
    
    def solve_kociemba(self, scramble="", pattern=None):
        c = cube.Cube()
        c.apply_moves(scramble)
        color_to_face = {'g': 'F', 'b': 'B', 'o': 'R', 'r': 'L', 'y': 'U', 'w': 'D'}
        cube_string = []

        for face in "urfdlb":
            for line in c.state[face]:
                for color in line:
                    cube_string.append(color_to_face[color])
        
        return kociemba.solve("".join(cube_string), pattern)

    def solve(self, scramble="", solve_method="kociemba", pattern=None):
        if pattern is not None:
            return self.solve_kociemba(scramble, pattern)

        match solve_method:
            case "CFOP":
                return self.solve_CFOP(scramble)
            case "kociemba":
                return self.solve_kociemba(scramble)