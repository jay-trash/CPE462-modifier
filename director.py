import os

def input_output():
    print(
        '''
        This program takes 4 inputs.
        1. The image you want to change (Input Image).
        2. The image that you want to extract data from to change the first image (Seed Image).
        3. The name of the output file with '.jpg' extension at the end.
        4. The program that you want to use on the images.
        Make sure that the seed images and python files are all in the same directory.
        ''')
    input_one = input('Write the name of your input image (with extension) and press ENTER\n')
    input_two = input('Write the name of your seed image (with extension) and press ENTER\n')
    input_three = input('Write the name of the output file with .jpg extension and press ENTER\n')
    print(
        '''
        These are the available python programs to choose from so far:
        Choice a: main.py
        Choice b: mattmain.py
        Choice c: jaworski_filter_generator.py
        Choice d: contraster.py
        Choice e: Iraklimain.py
        ''')

    input_four = input('Please write your choice letter for the program that you want to use and press ENTER\n')
    program_dict = {
        "a": "main.py",
        "b": "mattmain.py",
        "c": "jaworski_filter_generator.py",
        "d": "contraster.py"
        "e": "Iraklimain.py"
    }
    input_four_converted = program_dict[input_four]

    total_input = 'python' + ' ' + input_four_converted + ' ' + input_one + ' ' + input_two + ' ' + input_three
    os.system(total_input)


def main():
    input_output()

if __name__ == "__main__":
    main()
