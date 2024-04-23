import copy

def replace_column(matrix, j, col):
    for i, val in enumerate(col):
        matrix[i][j] = val

class Cube():
    def __init__(self):
        self.state = {'f': [['g'] * 3 for _ in range(3)],
                      'b': [['b'] * 3 for _ in range(3)],
                      'r': [['o'] * 3 for _ in range(3)],
                      'l': [['r'] * 3 for _ in range(3)],
                      'u': [['y'] * 3 for _ in range(3)],
                      'd': [['w'] * 3 for _ in range(3)]}
        
    def rotate_face_clockwise(self, side):
        face = [[''] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                face[j][2 - i] = self.state[side][i][j]

        self.state[side] = face

    def rotate_U_layer(self, count=1):
        for _ in range(count):
            self.rotate_face_clockwise('u')
            temp = self.state['f'][0]
            self.state['f'][0] = self.state['r'][0]
            self.state['r'][0] = self.state['b'][0]
            self.state['b'][0] = self.state['l'][0]
            self.state['l'][0] = temp

    def rotate_D_layer(self, count=1):
        for _ in range(count):
            self.rotate_face_clockwise('d')
            temp = self.state['f'][2]
            self.state['f'][2] = self.state['l'][2]
            self.state['l'][2] = self.state['b'][2]
            self.state['b'][2] = self.state['r'][2]
            self.state['r'][2] = temp

    def rotate_R_layer(self, count=1):
        for _ in range(count):
            self.rotate_face_clockwise('r')
            temp = [line[2] for line in self.state['f']]
            replace_column(self.state['f'], 2, [line[2] for line in self.state['d']])
            replace_column(self.state['d'], 2, [line[0] for line in self.state['b']][::-1])
            replace_column(self.state['b'], 0, [line[2] for line in self.state['u']][::-1])
            replace_column(self.state['u'], 2, temp)

    def rotate_L_layer(self, count=1):
        for _ in range(count):
            self.rotate_face_clockwise('l')
            temp = [line[0] for line in self.state['f']]
            replace_column(self.state['f'], 0, [line[0] for line in self.state['u']])
            replace_column(self.state['u'], 0, [line[2] for line in self.state['b']][::-1])
            replace_column(self.state['b'], 2, [line[0] for line in self.state['d']][::-1])
            replace_column(self.state['d'], 0, temp)

    def rotate_F_layer(self, count=1):
        for _ in range(count):
            self.rotate_face_clockwise('f')
            temp = self.state['u'][2]
            self.state['u'][2] = [line[2] for line in self.state['l']][::-1]
            replace_column(self.state['l'], 2, self.state['d'][0])
            self.state['d'][0] = [line[0] for line in self.state['r']][::-1]
            replace_column(self.state['r'], 0, temp)

    def rotate_B_layer(self, count=1):
        for _ in range(count):
            self.rotate_face_clockwise('b')
            temp = self.state['u'][0]
            self.state['u'][0] = [line[2] for line in self.state['r']]
            replace_column(self.state['r'], 2, self.state['d'][2][::-1])
            self.state['d'][2] = [line[0] for line in self.state['l']]
            replace_column(self.state['l'], 0, temp[::-1])

    def apply_moves(self, moves): 
        # TODO: maybe implement wide moves / rotations / slice moves
        cube_copy = copy.deepcopy(self.state)
        for move in moves.split():
            match move:
                case "U": self.rotate_U_layer()
                case "U2": self.rotate_U_layer(2)
                case "U'": self.rotate_U_layer(3)
                case "D": self.rotate_D_layer()
                case "D2": self.rotate_D_layer(2)
                case "D'": self.rotate_D_layer(3)
                case "F": self.rotate_F_layer()
                case "F2": self.rotate_F_layer(2)
                case "F'": self.rotate_F_layer(3)
                case "B": self.rotate_B_layer()
                case "B2": self.rotate_B_layer(2)
                case "B'": self.rotate_B_layer(3)
                case "R": self.rotate_R_layer()
                case "R2": self.rotate_R_layer(2)
                case "R'": self.rotate_R_layer(3)
                case "L": self.rotate_L_layer()
                case "L2": self.rotate_L_layer(2)
                case "L'": self.rotate_L_layer(3)
                case _: 
                    print("Invalid move inputted. All other moves were reverted.")
                    self.state = cube_copy
                    break

    def print_cube(self):
        for face in 'ulfrdb':
            print(face, end=': \n')
            for line in self.state[face]:
                print(line)
            print()
    
    def pprint_cube(self):
        for line in self.state['u']:
            print(f'    {"".join(line)}')
        print()
        for i in range(3):
            print("".join(self.state['l'][i]), "".join(self.state['f'][i]), "".join(self.state['r'][i]))
        print()
        for line in self.state['d']:
            print(f'    {"".join(line)}')
        print()
        for row in reversed(self.state['b']):
            print(f'    {"".join(reversed(row))}')
        
if __name__ == "__main__":
    cube = Cube()
    cube.apply_moves("R U R' U' R' F R2 U' R' U' R U R' F'")
    cube.pprint_cube()
    print("------------------")
    cube.apply_moves("R U R' U' R' F R2 U' R' U' R U R' F'")
    cube.pprint_cube()
