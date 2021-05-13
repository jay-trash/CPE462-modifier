import os

def input_output():
    print(
        '''
        This program takes 5 inputs.
        1. The image you want to change (Input Image).
        2. The image that you want to extract data from to change the first image (Seed Image).
        3. The name of the output file with '.jpg' extension at the end.
        4. The program that you want to use on the images.
        5. Your version of python.
        Make sure that the seed images and python files are all in the same directory.
        ''')
    input_one = input('   Type the name of your input image (with extension) and press ENTER\n')
    input_two = input('   Type the name of your seed image (with extension) and press ENTER\n')
    input_three = input('   Type the name of the output file with .jpg extension and press ENTER\n')
    print(
        '''
        These are the available python programs to choose from so far:
        Choice a: mattmain.py
        Choice b: pattern_generator.py
        Choice c: Iraklimain.py
        Choice d: jaworski_filter_generator.py
        Choice e: contraster.py
        ''')

    input_four = input('    Please type your choice letter for the program that you want to use and press ENTER\n')
    program_dict = {
        "a": "mattmain.py",
        "b": "pattern_generator.py",
        "c": "Iraklimain.py",
        "d": "jaworski_filter_generator.py",
        "e": "contraster.py",
    }
    input_four_converted = program_dict[input_four]

    input_python = input('  How is python called on your system? (For example "python" or "python3")\n')

    total_input = input_python + ' ' + input_four_converted + ' ' + input_one + ' ' + input_two + ' ' + input_three
    os.system(total_input)


def main():
    input_output()

if __name__ == "__main__":
    main()
