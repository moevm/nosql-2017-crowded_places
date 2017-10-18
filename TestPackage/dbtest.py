from pymongo import MongoClient


def main():
    connection = MongoClient("nick1-Lenovo-IdeaPad-Y550P")
    db = connection.test1.test2
    # student_record = {'name': "student_name1", 'grade': "student_grade"}
    # insert the record
    # db.insert(student_record)
    allDocs = db.find({"name":"student_name"})
    for record in allDocs:
        print(record)
    connection.close()
    return

if __name__ == "__main__":
    main()