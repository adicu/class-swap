import pymongo, json

MONGODB_URI = 'mongodb://parser:parser@ds049661.mongolab.com:49661/class-swap'
CURRENT_TERM = "20151"    # update for every term
COURSE_FILENAME = "./doc.json"
KEYS = ['Term', 'Course', 'PrefixName', 'DepartmentCode', 'DepartmentName', 
        'CallNumber', 'NumEnrolled', 'MaxSize', 'CourseTitle', 'CourseSubtitle', 
        'PrefixLongname', 'Meets1', 'Meets2', 'Meets3', 'Meets4', 'Meets5', 'Meets6', 
        'Instructor1Name']

def get_courses():
    client = pymongo.MongoClient(MONGODB_URI)
    db = client['class-swap']
    return db.courses

def parse(course_file):
    '''Parse JSON data'''
    raw_data = json.load(course_file)
    # relevant keys are:
    # term, course, prefixname, departmentcode, departmentname, callnumber, numenrolled, maxsize, coursetitle, coursesubtitle, prefixlongname, meets#, instructorname
    
    course_data = []
    # pull in relevant courses and data
    for course in raw_data:
        entry = {}
        if course['Term'] == CURRENT_TERM and course['DepartmentCode'] == "AHAR":
            for key in KEYS:
                if course[key] != "":
                    entry[key] = course[key]
            course_data.append(entry)

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
