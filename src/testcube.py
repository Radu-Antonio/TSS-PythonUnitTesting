from src.cube import Cube
import unittest

class TestCube(unittest.TestCase):

    def testConstruction(self):
        sampleCube = Cube()
        emptyCubeToTest = {'f': [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
        'b': [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']], 
        'r': [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']], 
        'l': [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']], 
        'u': [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']], 
        'd': [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]}

        self.assertEqual(sampleCube.state, emptyCubeToTest)

    def test_Rotate_Face_Clock_Wise_One_Time(self):
        sampleCube = Cube()
        sampleFace = [['g', 'b', 'g'], ['b', 'o', 'r'], ['w', 'y', 'r']]
        sampleCube.state['f'] = sampleFace
        sampleCube.rotate_face_clockwise('f')

        self.assertEqual(sampleCube.state['f'], [['w', 'b', 'g'], ['y', 'o', 'b'], ['r', 'r', 'g']])

    def test_Rotate_Face_Clock_Wise_Two_Times(self):
        sampleCube = Cube()
        sampleFace = [['g', 'b', 'g'], ['b', 'o', 'r'], ['w', 'y', 'r']]
        sampleCube.state['f'] = sampleFace
        sampleCube.rotate_face_clockwise('f')
        sampleCube.rotate_face_clockwise('f')

        self.assertEqual(sampleCube.state['f'], [['r', 'y', 'w'], ['r', 'o', 'b'], ['g', 'b', 'g']])

    def test_Rotate_Face_Counter_ClockWise(self):
        sampleCube = Cube()
        sampleFace = [['g', 'b', 'g'], ['b', 'o', 'r'], ['w', 'y', 'r']]
        sampleCube.state['f'] = sampleFace
        sampleCube.rotate_face_clockwise('f')
        sampleCube.rotate_face_clockwise('f')
        sampleCube.rotate_face_clockwise('f')

        self.assertEqual(sampleCube.state['f'], [['g', 'r', 'r'], ['b', 'o', 'y'], ['g', 'b', 'w']])

    def test_Rotate_U_Layer(self):
        sampleCube = Cube()
        sampleFace = [['g', 'b', 'g'], ['b', 'o', 'r'], ['w', 'y', 'r']]
        sampleCube.state['u'] = sampleFace
        sampleCube.rotate_U_layer()

        testState = {'f': [['o', 'o', 'o'], ['g', 'g', 'g'], ['g', 'g', 'g']],
        'b': [['r', 'r', 'r'], ['b', 'b', 'b'], ['b', 'b', 'b']], 
        'r': [['b', 'b', 'b'], ['o', 'o', 'o'], ['o', 'o', 'o']], 
        'l': [['g', 'g', 'g'], ['r', 'r', 'r'], ['r', 'r', 'r']], 
        'u': [['w', 'b', 'g'], ['y', 'o', 'b'], ['r', 'r', 'g']], 
        'd': [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]}

        self.assertEqual(testState, sampleCube.state)

    def test_Rotate_D_Layer(self):
        sampleCube = Cube()
        sampleFace = [['g', 'b', 'g'], ['b', 'o', 'r'], ['w', 'y', 'r']]
        sampleCube.state['d'] = sampleFace
        sampleCube.rotate_D_layer()

        testState = {'f': [['g', 'g', 'g'], ['g', 'g', 'g'], ['r', 'r', 'r']],
        'b': [['b', 'b', 'b'], ['b', 'b', 'b'], ['o', 'o', 'o']], 
        'r': [['o', 'o', 'o'], ['o', 'o', 'o'], ['g', 'g', 'g']], 
        'l': [['r', 'r', 'r'], ['r', 'r', 'r'], ['b', 'b', 'b']], 
        'u': [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']], 
        'd': [['w', 'b', 'g'], ['y', 'o', 'b'], ['r', 'r', 'g']]}

        self.assertEqual(testState, sampleCube.state)

    def test_Rotate_R_Layer(self):
        sampleCube = Cube()
        sampleFace = [['g', 'b', 'g'], ['b', 'o', 'r'], ['w', 'y', 'r']]
        sampleCube.state['r'] = sampleFace
        sampleCube.rotate_R_layer()
        self.maxDiff = None
        testState = {'f': [['g', 'g', 'w'], ['g', 'g', 'w'], ['g', 'g', 'w']],
        'b': [['y', 'b', 'b'], ['y', 'b', 'b'], ['y', 'b', 'b']], 
        'r': [['w', 'b', 'g'], ['y', 'o', 'b'], ['r', 'r', 'g']], 
        'l': [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']], 
        'u': [['y', 'y', 'g'], ['y', 'y', 'g'], ['y', 'y', 'g']], 
        'd': [['w', 'w', 'b'], ['w', 'w', 'b'], ['w', 'w', 'b']]}

        self.assertEqual(testState, sampleCube.state)

    def test_Rotate_L_Layer(self):
        sampleCube = Cube()
        sampleFace = [['g', 'b', 'g'], ['b', 'o', 'r'], ['w', 'y', 'r']]
        sampleCube.state['l'] = sampleFace
        sampleCube.rotate_L_layer()
        self.maxDiff = None
        testState = {'f': [['y', 'g', 'g'], ['y', 'g', 'g'], ['y', 'g', 'g']],
        'b': [['b', 'b', 'w'], ['b', 'b', 'w'], ['b', 'b', 'w']], 
        'r': [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']], 
        'l': [['w', 'b', 'g'], ['y', 'o', 'b'], ['r', 'r', 'g']], 
        'u': [['b', 'y', 'y'], ['b', 'y', 'y'], ['b', 'y', 'y']], 
        'd': [['g', 'w', 'w'], ['g', 'w', 'w'], ['g', 'w', 'w']]}

        self.assertEqual(testState, sampleCube.state)

    def test_Rotate_F_Layer(self):
        sampleCube = Cube()
        sampleFace = [['g', 'b', 'g'], ['b', 'o', 'r'], ['w', 'y', 'r']]
        sampleCube.state['f'] = sampleFace
        sampleCube.rotate_F_layer()
        self.maxDiff = None
        testState = {'f': [['w', 'b', 'g'], ['y', 'o', 'b'], ['r', 'r', 'g']],
        'b': [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']], 
        'r': [['y', 'o', 'o'], ['y', 'o', 'o'], ['y', 'o', 'o']], 
        'l': [['r', 'r', 'w'], ['r', 'r', 'w'], ['r', 'r', 'w']], 
        'u': [['y', 'y', 'y'], ['y', 'y', 'y'], ['r', 'r', 'r']], 
        'd': [['o', 'o', 'o'], ['w', 'w', 'w'], ['w', 'w', 'w']]}

        self.assertEqual(testState, sampleCube.state)

    def test_Rotate_B_Layer(self):
        sampleCube = Cube()
        sampleFace = [['g', 'b', 'g'], ['b', 'o', 'r'], ['w', 'y', 'r']]
        sampleCube.state['b'] = sampleFace
        sampleCube.rotate_B_layer()
        self.maxDiff = None
        testState = {'f': [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
        'b': [['w', 'b', 'g'], ['y', 'o', 'b'], ['r', 'r', 'g']], 
        'r': [['o', 'o', 'w'], ['o', 'o', 'w'], ['o', 'o', 'w']], 
        'l': [['y', 'r', 'r'], ['y', 'r', 'r'], ['y', 'r', 'r']], 
        'u': [['o', 'o', 'o'], ['y', 'y', 'y'], ['y', 'y', 'y']], 
        'd': [['w', 'w', 'w'], ['w', 'w', 'w'], ['r', 'r', 'r']]}

        self.assertEqual(testState, sampleCube.state)

    def test_apply_moves(self):
        #testing all possible moves:
        sampleCube = Cube()
        sampleCube.apply_moves("U D U2  L2 D2 R2 D' F R' F2 F' B  U' R D2 B' L B2 L'")
        #w -> y; y -> r; w2 -> w
        testCube = {'f': [['g', 'b', 'b'], ['b', 'g', 'r'], ['b', 'g', 'r']],
        'b': [['o', 'y', 'o'], ['g', 'b', 'y'], ['o', 'o', 'g']], 
        'r': [['r', 'r', 'g'], ['y', 'o', 'w'], ['w', 'o', 'w']], 
        'l': [['g', 'w', 'w'], ['b', 'r', 'o'], ['r', 'g', 'y']], 
        'u': [['w', 'g', 'y'], ['r', 'y', 'b'], ['r', 'w', 'y']], 
        'd': [['o', 'r', 'b'], ['o', 'w', 'w'], ['y', 'y', 'b']]}

        self.assertEqual(sampleCube.state, testCube)

    def test_invalid_move(self):
        sampleCube = Cube()
        sampleCube.apply_moves("U D A B2")

        emptyTestCube = {'f': [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
        'b': [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']], 
        'r': [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']], 
        'l': [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']], 
        'u': [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']], 
        'd': [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]}

        self.assertEqual(sampleCube.state, emptyTestCube)