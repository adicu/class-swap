import pymongo, bson, json, db

MONGODB_URI = "mongodb://parser:parser@ds049661.mongolab.com:49661/class-swap"

# submit user"s course to database
def put_course(uni, call_num):
    listed = db.get_listed()
    entry = {"uni": uni, "CallNumber": call_num, "status": "open"}
    listed.insert(entry)

# update status of user-listed course
def update_course(uni, call_num, status):
    listed = db.get_listed()
    entry = {"uni": uni, "CallNumber": call_num, "status": status}
    listed.update({"uni": uni, "CallNumber": call_num}, entry, False)

# list search results
def list_courses(course, instructor, time):
    listed = db.get_listed()
    courses = db.get_courses()
    # make search query
    query = {}
    results = []
    if course:
        query["Course"] = { "$regex": "^" + course }
    if instructor:
        query["Instructor1Name"] = instructor
    if time:
        query["Meets1"] = time
    for doc in courses.find(query):
        uquery = {"CallNumber": doc["CallNumber"], "status": "open"}
        listing = {}
        for user in listed.find(uquery):
            listing["uni"] = user["uni"]
            listing["CallNumber"] = doc["CallNumber"]
            listing["Course"] = doc["Course"]
            listing["InstructorName"] = doc["Instructor1Name"]
            listing["Meets"] = doc["Meets1"]
            listing["status"] = user["status"]
            results.append(listing)
    return results