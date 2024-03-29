# Created by: Luke Heary
# Date: 12/9/19
import sys


def main():
    data_file = sys.argv[1]
    n = int(sys.argv[2])

    unique_names = set()
    unique_first_names = set()
    unique_last_names = set()
    most_common_first_names = dict()
    most_common_last_names = dict()

    already_have_seen = set()
    specifically_unique = set()

    # Opens the data file and reads one line into memory at once
    with open(data_file) as FileObj:
        for count, line in enumerate(FileObj, start=1):
            # Gets every other line (because every other line is a name)
            if count % 2 == 1:
                cleaned_line = line.replace(" ", "")
                cleaned_line = cleaned_line.split("--")
                cleaned_line = cleaned_line[0].split(",")
                first_name = cleaned_line[1]
                last_name = cleaned_line[0]
                unique_names.add(first_name + " " + last_name)
                unique_first_names.add(first_name)
                unique_last_names.add(last_name)

                # These two if statements figure out the most common First and Last names
                if first_name not in most_common_first_names:
                    most_common_first_names[first_name] = 0
                else:
                    most_common_first_names[first_name] += 1

                if last_name not in most_common_last_names:
                    most_common_last_names[last_name] = 0
                else:
                    most_common_last_names[last_name] += 1

                # This set of if statements figures out if the names are specifically unique
                if first_name not in already_have_seen:
                    if last_name not in already_have_seen:
                        specifically_unique.add(first_name + " " + last_name)
                    else:
                        already_have_seen.add(last_name)
                else:
                    already_have_seen.add(first_name)

    # Gets the most common first name, and the how many times it shows up
    most_common_first_name = max(most_common_first_names, key=most_common_first_names.get)
    most_common_first_name_count = str(most_common_first_names[most_common_first_name])

    # Gets the most common last name, and the how many times it shows up
    most_common_last_name = max(most_common_last_names, key=most_common_last_names.get)
    most_common_last_name_count = str(most_common_last_names[most_common_last_name])

    # Gets the n amount of specifically unique names and appends them to a string for printing
    specifically_unique_list = list(specifically_unique)
    specifically_unique_list_length_n = list()
    for i in range(n):
        specifically_unique_list_length_n.append(specifically_unique_list[i])

    specifically_unique_string = ""
    list_length_counter = 0
    for name in specifically_unique_list_length_n:
        specifically_unique_string += name
        list_length_counter += 1
        if list_length_counter != n: specifically_unique_string += ", "

    # Creates the modified names and puts them into a new string for printing
    first_names = list()
    last_names = list()
    for name in specifically_unique_list_length_n:
        name_attributes = name.split(" ")
        first_names.append(name_attributes[0])
        last_names.append(name_attributes[1])

    modified_names_string = ""
    index_counter = 1
    list_length_counter = 0
    while list_length_counter < n:
        modified_names_string += first_names[list_length_counter] + " " + last_names[index_counter]
        index_counter += 1
        list_length_counter += 1
        if list_length_counter is not n: modified_names_string += ", "
        if index_counter == n:
            index_counter = 0


    print "1. Unique Count of Full Names: " + str(len(unique_names))
    print "2. Unique Count of First Names: " + str(len(unique_first_names))
    print "3. Unique Count of Last Names: " + str(len(unique_last_names))
    print "4. Most Common First Name: " + most_common_first_name + " (appears " + most_common_first_name_count + " times)"
    print "5. Most Common Last Name: " + most_common_last_name + " (appears " + most_common_last_name_count + " times)"

    print "6. " + str(n) + " Specifically Unique Names: " + specifically_unique_string
    print "7. " + str(n) + " Modified Names: " + modified_names_string


if __name__ == "__main__":
    main()
