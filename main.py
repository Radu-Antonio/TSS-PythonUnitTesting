# import sys
# print(sys.path)
import cube
import solver
import scrambler 


class mainApp():
    def play():
        sol = solver.Solver()
        scr = scrambler.Scrambler()

        while True:
            option = input("1 for solver, 2 for scrambler, anything else for exit: ")
            if option not in "12":
                break
            elif option == '1':
                sc = input("input valid scramble for the solver: ").split()
                if len(sc) < 15:
                    raise Exception("scramble should have at least 15 moves")
                if set(sc) - set(scrambler.legal_moves):
                    raise Exception("scramble contains non-legal moves")
                solution = sol.solve(" ".join(sc))
                print(f"solution: {solution}")
            else:
                seed = int(input("Introduce a seed (0-1000) for the scrambler: "))
                scram = scr.generate_scramble(seed)
                print(f'scramble generated: {scram}')
                ans = input("Do you want to solve the scramble ? (y/n)")
                if ans == 'y':
                    print(f"solution: {sol.solve(scram)}")


if __name__ == "__main__":
    mainApp.play()