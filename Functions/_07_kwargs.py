# Python **kwargs
def student_info(**details):
    print(details)
    print("name: ",details["name"])


student_info(name="Jeel", age=20)
student_info(name="Rahul", age=21, course="BTech IT")