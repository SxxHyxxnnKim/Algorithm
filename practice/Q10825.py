class ClassRoom:
    #학생 정보 저장할 리스트
    students = []

    def __init__(self, count):
        #학생수 변수
        self.count = count
        #리스트 초기화
        self.students = []

    def insertScore(self, data):
        
        data = data.split(" ")

        #각각의 학생 정보를 딕셔너리로 저장하기 위한 변수
        student = {}

        student["name"] = data[0]
        student["kor"] = int(data[1])
        student["eng"] = int(data[2])
        student["math"] = int(data[3])
        
        self.students.append(student)

    def sortStudent(self, students):
        students.sort(key = lambda x: (100-x["kor"], x["eng"], 100-x["math"], x["name"])) 

classRoom = ClassRoom(int(input()))
for i in range(classRoom.count):
    classRoom.insertScore(input())

classRoom.sortStudent(classRoom.students)

for i in classRoom.students:
    print(i["name"])

    