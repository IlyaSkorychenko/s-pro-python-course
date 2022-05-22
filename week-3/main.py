from word_utils import get_words, get_the_longest_word


def read_file_by_line(file_name: str):
    file = open(file_name)
    line_id = 0

    while True:
        line_id += 1
        line = file.readline()

        if not line:
            break

        yield line_id, line

    file.close()


if __name__ == '__main__':
    # task-1
    initial_file_name = input("File name to read from: ")
    destination_file_name = input("File name to write from: ")
    file_write_to = open(destination_file_name, 'w')

    for line_id, line in read_file_by_line(initial_file_name):
        file_write_to.write(f'{line_id}: {line}')

    file_write_to.close()

    # task-2
    sent = "If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing " \
           "hidden in the middle of text."
    words = get_words(sent)
    print(words)
    te_longer = get_the_longest_word(words)
    print(te_longer)
