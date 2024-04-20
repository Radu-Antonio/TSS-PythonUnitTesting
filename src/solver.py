import kociemba
import cube 

class Solver():
    def solve_CFOP(self, scramble=""):
        c = cube.Cube()
        c.apply_moves(scramble)
        solution = []
        # TODO
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

if __name__ == "__main__":
    solver = Solver()
    solution = solver.solve(scramble="R' B2 R2 D' L2 F2 U F2 D2 R2 D' B2 L' F2 D' R2 B R' D U2 B'")
    # solution = solver.solve(scramble="R U R' U' R' F R2 U' R' U' R U R' F'")
    print(solution)