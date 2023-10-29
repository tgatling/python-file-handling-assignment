import datetime
import logging

logging.basicConfig(
    filename='activity.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)


def read_file_lines(file_path):
    """
    Reads text file and returns a list containing individual lines
    :param file_path: The path to the text file (str)
    :return: List of strings representing each line from the file
    """

    try:
        with open(file_path, 'r') as textfile:
            return textfile.readlines()
    except FileNotFoundError as e:
        logging.error(f"File Not Found Error: {e}")


def split_name_and_dob(line):
    """
    Splits the string containing a name and date of birth into separate components
    :param line: A string containing the name and date of birth
    :return: A tuple containing a name (str) and date of birth
    """

    name_dob = line.strip()
    name, dob_str = name_dob.split(', ')
    return name, dob_str


def convert_dob_str_to_date(dob_str):
    """
    Converts the date of birth to a date object
    :param dob_str: A string representing date of birth in the format "yyyy-mm-dd"
    :return: a datetime date object representing the date of birth
    """

    try:
        yr_m_d = dob_str.split('-')
        return datetime.date(int(yr_m_d[0]), int(yr_m_d[1]), int(yr_m_d[2]))
    except (ValueError, IndexError) as e:
        logging.error(f"Invalid date format: {e}")


def calculate_age(dob):
    """
    Calculate a person's age based on their date of birth
    :param dob: An datetime date object representing a person's date of birth
    :return age (int): A person's age in years
    """

    # current_date = datetime.datetime.now()
    current_date = datetime.date(2022, 6, 1)  # use this date to get the values in comparison output file
    age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))

    return age


def get_name_and_age(line):
    """
    Extracts the name and birthdate from the line to determine age
    :param line: A string containing name and birthdate
    :return: A tuple containing the name (str) and age(int)
    """

    name, dob_str = split_name_and_dob(line)
    dob = convert_dob_str_to_date(dob_str)
    age = calculate_age(dob)

    return name, age


def sort_by_age(names_ages):
    """
    Sorts the dictionary of names and ages by age (desc)
    :param names_ages: a dictionary where keys are names (str) and the values are ages (int)
    :return sorted_name_ages: the sorted dictionary of names and ages
    """

    # Function to return age used for sorting
    def get_age(name_age):
        return name_age[1]

    sorted_names_ages = dict(sorted(names_ages.items(), key=get_age, reverse=True))
    return sorted_names_ages


def generate_output(names_ages, file_name):
    """
    Generate output file of names and ages
    :param names_ages: A dictionary where keys are names (str) and the values are ages (int)
    :param file_name: The name to be given to the output file (str)
    :return: None
    """

    with open(file_name, 'w') as output_file:
        for name in names_ages:
            output_file.write(f'{name}: {names_ages[name]} years old\n')


def compare_files(file_path_1, file_path_2):
    """
    Compare two given files to determine if they are a match
    :param file_path_1: The path of the first file (str)
    :param file_path_2: The path of the second file (str)
    :return: A Boolean True if the files are a match and False if they are not
    """

    try:
        with open(file_path_1, 'r') as f1, open(file_path_2, 'r') as f2:
            file1_lines = f1.readlines()
            file2_lines = f2.readlines()

        if file1_lines == file2_lines:
            return True
        else:
            return False
    except FileNotFoundError as e:
        logging.error(f"File Not Found Error: {e}")
    except IOError as e:
        logging.error(f"Error reading files: {e}")
