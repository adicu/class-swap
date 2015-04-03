import pymongo, json

MONGODB_URI = 'mongodb://parser:parser@ds049661.mongolab.com:49661/class-swap'
CURRENT_TERM = "20151"    # update for every term
COURSE_FILENAME = "./doc.json"
# relevant keys from course data provided by CUIT
KEYS = ['Term', 'Course', 'PrefixName', 'DepartmentCode', 'DepartmentName', 
        'CallNumber', 'NumEnrolled', 'MaxSize', 'CourseTitle', 'CourseSubtitle', 
        'PrefixLongname', 'Meets1', 'Meets2', 'Meets3', 'Meets4', 'Meets5', 'Meets6', 
        'Instructor1Name']
# relevant classes
CLASSES = ["SCNC1100", "HUMA1121", "HUMA1123", "HUMA1001", "HUMA1002",
           "COCI1101", "COCI1102", "ENGL1010", "ENGL1011", "ENGL1012",
           "ENGL1013", "ENGL1014", "ENGL1020"]             
             
def get_courses():
    client = pymongo.MongoClient(MONGODB_URI)
    db = client['class-swap']
    return db.courses

def parse(course_file):
    '''Parse JSON data'''
    raw_data = json.load(course_file)
   
    course_data = []
    # pull in relevant courses and data
    for course in raw_data:
        entry = {}
        if course['Term'] != CURRENT_TERM:
            continue
        for c in CLASSES:
            if c not in course['Course']:
                continue
            for key in KEYS:
                if course[key] != "":
                    entry[key] = course[key]
            course_data.append(entry)
            break

    return course_data

def update(db, data):
    for course in data:
        courses.update({'CallNumber': course['CallNumber']}, course, True)

# main function
if __name__ == "__main__":
    courses = get_courses()
    with open(COURSE_FILENAME) as course_file:
        course_data = parse(course_file)
    update(courses, course_data)
