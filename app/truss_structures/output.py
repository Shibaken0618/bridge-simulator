import os

from structures.out.svg import structure_solution_to_svg
from structures.out.text import structure_solution_to_string
from structures.solution.structure import StructureSolution

# create an svg of the final solution of the simulation
def save_solution_to_svg(solution: StructureSolution, arguments):
    solution_svg = structure_solution_to_svg(solution, arguments)
    __write_to_file('result.svg', solution_svg)

# create a text file of the final result of the simulation
def save_solution_to_text(solution: StructureSolution):
    solution_text = structure_solution_to_string(solution)
    __write_to_file('result.txt', solution_text)

# save results into a file
def __write_to_file(filename, content):
    file_path = os.path.join(os.getcwd(), filename)
    with open(file_path, 'w') as file:
        file.write(content)