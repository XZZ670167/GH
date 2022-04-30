
def draw_stars(coded_str):
    # coded string is a comma deliminated string
    # string segment consist of a character to be printed (e.g. *) followed by
    # digit which is the number of times the character is to be printed
    to_print_instructions = coded_str.split(",")
    for instruction in to_print_instructions:
        character_to_print = instruction[0]
        number_repeats = int(instruction[1:])
        result = ""
        for repeat in range(number_repeats):
            result = result + character_to_print
        print(result, end='')

    print("\n")


def draw_box():
    # draw a box
    draw_stars(" 5,*10")
    for repeat in range(4):
        draw_stars(" 5,*1, 8,*1")
    draw_stars(" 5,*10")


def draw_broken_line():
    draw_stars(" 5,*5, 2,*10, 3,*20")


def main():
    draw_box()


if __name__ == "__main__":
    main()
