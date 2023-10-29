import fileFunctions

# Files
people_dob_file = 'People_And_Their_DOBs.txt'
comparison_output_file = 'People_And_Their_DOBs_Output.txt'
generated_output_file = 'People_And_Their_DOBs_Output_Tequesha.txt'

# Dictionary for storing names and ages
names_ages = {}

if __name__ == '__main__':

    file_lines = fileFunctions.read_file_lines(people_dob_file)

    # Create dictionary of names and ages
    if file_lines is None:
        fileFunctions.logging.error("Error: Unable to read file.")
    else:
        for line in file_lines:
            name, age = fileFunctions.get_name_and_age(line)
            names_ages[name] = age

    sorted_names_ages = fileFunctions.sort_by_age(names_ages)

    # Create output file with names and ages
    try:
        fileFunctions.generate_output(sorted_names_ages, generated_output_file)
    except IOError as e:
        fileFunctions.logging.error(f"Error writing the output file: {e}")

    # Compare the given output file with the newly generated file
    matched_and_verified = fileFunctions.compare_files(comparison_output_file, generated_output_file)

    if matched_and_verified:
        print('Matched and Verified')
    else:
        print('Files Do Not Match')
