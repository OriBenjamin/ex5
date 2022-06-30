import json
import os



def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".

    :param input_json_path: Path of the students database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.
    """
    registered_students = []
    with open(input_json_path, 'r') as f:
        student_data = json.load(f)
        for id in student_data.keys():
            student_courses = student_data[id]["registered_courses"]
            if course_name in set(student_courses):
                registered_students.append(student_data[id]["student_name"])
    return registered_students  

def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    enrollment_dictionary = {}
    with open(input_json_path, 'r') as f:
        student_data = json.load(f)
        for id in student_data.keys():
            for course in student_data[id]["registered_courses"]:
                if course in enrollment_dictionary:
                    enrollment_dictionary[course] += 1
                else:
                    enrollment_dictionary[course] = 1
    with open(output_file_path, 'w') as f:
        for course, students_number in sorted(enrollment_dictionary.items()):
            output_line = '"' + course + '" ' + str(students_number) + '\n'
            f.write(output_line)

def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    lecturesCourses = {}
    for filename in os.listdir(json_directory_path):
            if filename.endswith(".json"):
                with open(os.path.join(json_directory_path, filename), 'r') as file:
                    fileData = json.load(file)
                    for courseData in fileData.values():
                        courseName = list(courseData.values())[0]
                        lecturesList = list(courseData.values())[1]
                        for lecturerName in lecturesList:
                            if(not lecturerName in lecturesCourses):
                                lecturesCourses[lecturerName] = [courseName]
                            else:
                                if(lecturesCourses[lecturerName].count(courseName) == 0):
                                    lecturesCourses[lecturerName].append(courseName)
            else:
                continue

    with open(output_json_path, 'w') as outputFile:
        json.dump(lecturesCourses, outputFile, indent = 4)
       
            



