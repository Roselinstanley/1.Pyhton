class multiplecalc():
    num=0
    gender=" "
    age=0
    height=0
    breadth=0
    h1=0
    h2=0
    breadth1=0
    def __init__(self,n,gender,age,h,b,h1,h2,b1):
        self.num=n        #assigning value to class variable
        self.gender=gender
        self.age=age
        self.height=h
        self.breadth=b
        self.h1=h1
        self.h2=h2
        self.breadth1=b1
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Computer Vision")
        print("Robotics")
        print("Speech Processing")  
        print("Natural Language Processing")  
        return
    def OddorEven(self):
        if(self.num%2==0):
            print("The number is Even")
        else:
           print("The number is Odd")
        return 
    def eligibility(self):
        print("Gender=",self.gender)
        print("Age=",self.age)
        if(self.gender=="Male" and self.age >=21):
            print("This male is eligible for marriage")
        elif(self.gender=="Female" and self.age >=18):
            print("This female is eligible for marriage")
        else:
            print("Not eligible for marriage")
        return
    def percentage():
        Total=0
        marklist=[]
        m=1
        for i in range(0,5):
            mark=int(input("Enter subject mark"))
            marklist.append(mark)
            Total=Total+mark
        for j in marklist:
            print("Subject",m,"mark",j)
            m=m+1
        print("The Total mark is",Total) 
        percent=Total/500*100
        print("The Percentage is ",percent)   
        return
    def trianglearea(self):
        area=(self.height*self.breadth)/2
        print("Height of the triangle=",self.height)
        print("Breadth of the triangle=",self.breadth)
        print("Area of the triangle=",area)
        return
    def triangleperimeter(self):
        p=self.h1+self.h2+self.breadth1
        print("\n\nHeight1 of the triangle=",self.h1)
        print("Height2 of the triangle=",self.h2)
        print("Breadth of the triangle=",self.breadth1)
        print("Perimeter of the triangle=",p)
        return