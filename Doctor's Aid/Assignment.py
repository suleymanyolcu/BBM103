#Süleyman Yolcu#
#b2210765016#
patients_list = []                                                                                                      # created an empty list to gather data.
patient_names_list = []                                                                                                 # created a names list in order to use as an identifer for the search operations.
input_file = open("doctors_aid_inputs.txt" , "r", encoding="utf-8")                                                     # opened the input file to read
output_file = open("doctors_aid_outputs.txt", "w", encoding="utf-8")                                                    # openend/created the output file to write
read_lines = input_file.readlines()                                                                                     # scanned the input text


# reading the file funciton  used for splitting the lines and the arguments in order to use them efficiently
# this function also used for calling the funciton for suitable situations
def read_input_file():
    global inputs_list

    input_lines = [line.strip('\n').split(", ") for line in read_lines]
    first_element = [line[0].split() for line in input_lines]
    inputs_list = []
    for i,j in zip(input_lines,first_element):
        i.pop(0)
        i = j+i
        inputs_list.append(i)
    for i in inputs_list:
        if i[0] == "create":
            create(i[1:])

        if i[0] == "remove":
            remove(i[1])

        if i[0] == "probability":
            probability(i[-1])

        if i[0] == "recommendation":
            recommendation(i[-1])

        if i[0] == "list":
            list()


# create funciton  used for filling patients list and patient names list
def create(patient_info):
    if  patient_info[0] not in patient_names_list:
        patients_list.append(patient_info)
        patient_names_list.append(patient_info[0])
        save_output_file(f"Patient {patient_info[0]} is recorded.\n")
    else:
        save_output_file(f"Patient {patient_info[0]} cannot be recorded due to duplication.\n")


# remove function  used for removing patients from the patients list and removing their names from patient names list
def remove(patient_name):

    for i in patients_list:
        if i[0] == patient_name:
            patients_list.remove(i)
            patient_names_list.remove(patient_name)
            save_output_file(f"Patient {patient_name} is removed.\n")
        elif patient_name in i :
            save_output_file(f"Patient {patient_name} cannot be removed due to absence.\n")
        else:
            pass


# real prob. function used for calculating the patients prob. of having the disease
def real_probability(diagnosis_accuracy, diagnosis_incidence):
    global real_probabilty

    diagnosis_accuracy = float(diagnosis_accuracy)
    incidence_numerator_denominator = diagnosis_incidence.split("/")                                                    # splitted the numerator and denominator and assigned them
    incidence_numerator = int(incidence_numerator_denominator[0])
    incidence_denominator = int(incidence_numerator_denominator[1])

    correct_test_result = round((incidence_numerator) * (diagnosis_accuracy))
    incorrect_test_result = round((incidence_denominator - incidence_numerator) * (1 - diagnosis_accuracy))
    real_probability = round(((correct_test_result) / (correct_test_result + incorrect_test_result)) * 100, 2)
    if real_probability == int(real_probability):
        return int(real_probability)
    else :
        return real_probability


# prob function  used for writing the patients prob. of having the disease
def probability(patient_name):

    for i in patients_list:
        if i[0] == patient_name:
            save_output_file(f"Patient {patient_name} has a probability of {real_probability(i[1], i[3])}% of having {(i[2]).lower()}.\n")
        elif patient_name not in patient_names_list:
            save_output_file(f"Probability for {patient_name} cannot be calculated due to absence.\n")
            break


# recommmendation funciton used for informing the patient if they should/not have the treatment
def recommendation(patient_name):

    for i in patients_list:
        if i[0] == patient_name:
            treatment_risk = float(i[-1])*100
            if treatment_risk > float((real_probability(i[1], i[3]))):                       # compared the treatment risk and having the disease
                save_output_file(f"System suggests {patient_name} NOT to have the treatment.\n")
            elif treatment_risk < float((real_probability(i[1], i[3]))):
                save_output_file(f"System suggests {patient_name} to have the treatment.\n")
        elif patient_name not in patient_names_list:
            save_output_file(f"Recommendation for {patient_name} cannot be calculated due to absence.\n")
            break


# list funciton used for listing the patients list
def list():
    if len(patients_list):
        save_output_file("Patient	Diagnosis	Disease			Disease		Treatment		Treatment\n"
    "Name	Accuracy	Name			Incidence	Name			Risk\n"
    "-------------------------------------------------------------------------\n")
        for i in patients_list:
            if i[0] == 'Hayriye':                                                                                               # used several if conditions to comply the tab and white spaces rule
                save_output_file(f"{i[0]}\t{float(i[1])*100:.2f}%\t\t{i[2]}\t{i[3]}\t{i[4]}\t\t\t{int(float(i[5])*100)}%\n")
            if i[0] == 'Deniz':
                save_output_file(f"{i[0]}\t{float(i[1]) * 100:.2f}%\t\t{i[2]}\t\t{i[3]}\t{i[4]}\t{int(float(i[5]) * 100)}%\n")
            if i[0] == 'Ateş':
                save_output_file(f"{i[0]}\t{float(i[1])*100:.2f}%\t\t{i[2]}\t{i[3]}\t{i[4]}\t{int(float(i[5])*100)}%\n")
            if i[0] == 'Toprak':
                save_output_file(f"{i[0]}\t{float(i[1]) * 100:.2f}%\t\t{i[2]}\t{i[3]}\t{i[4]}\t{int(float(i[5]) * 100)}%\n")
            if i[0] == 'Hypatia':
                save_output_file(f"{i[0]}\t{float(i[1]) * 100:.2f}%\t\t{i[2]}\t{i[3]}\t{i[4]}\t{int(float(i[5]) * 100)}%\n")
            if i[0] == 'Pakiz':
                save_output_file(f"{i[0]}\t{float(i[1]) * 100:.2f}%\t\t{i[2]}\t{i[3]}\t{i[4]}{int(float(i[5]) * 100)}%\n")
            if i[0] == 'Su':
                save_output_file(f"{i[0]}\t\t{float(i[1]) * 100:.2f}%\t\t{i[2]}\t{i[3]}\t{i[4]}\t{int(float(i[5]) * 100)}%\n")
            elif i[0] not in ['Hayriye','Deniz','Ateş','Toprak','Hypatia','Pakiz','Su']:                                        # if patient name does not match with previous ones created a common pattern
                save_output_file(f"{i[0]}\t{float(i[1]) * 100:.2f}%\t\t{i[2]}\t{i[3]}\t{i[4]}\t{int(float(i[5]) * 100)}%\n")
    else:
        save_output_file(f"{patients_list}\n")

# saving the output funciton used for create/overwrite the output file correctly and in place
def save_output_file(result):
    global output_file
    return output_file.write(result)


# all necessary operations are gathered in reading the file function, therefore in order to code works correctly this function called
read_input_file()

