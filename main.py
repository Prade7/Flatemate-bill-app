from fpdf import FPDF
import webbrowser

class bill():
    def __init__(self,amount,period):

        """object that contain data about the bill that is the period and amount of bill"""

        self.amount=amount
        self.period=period

class flatmate():
    def __init__(self,name,days_in_house):

        """Object that contain data about the name and number of days that the person stayed in the flat"""

        self.name=name
        self.days_in_house=days_in_house

    
    def pays(self,flatmatePerson,the_bill):
        weight=self.days_in_house/(self.days_in_house+flatmatePerson.days_in_house)
        to_pay=the_bill.amount*weight
        return to_pay

    
class pfdGenerator():
    def __init__(self,filename):
        self.filename=filename

        """This class is used to generate pdf by using the flatemates data"""

    def generate(self,flatemate1,flatemate2,the_bill):
        pdf=FPDF(orientation="p",unit="pt",format="A4")
        pdf.add_page()
        pdf.set_font(family="Times",size=24,style="B")
        pdf.cell(w=0,h=80,txt="Flatemate Bill",border=1,align="C",ln=1)
        pdf.set_font(family="Times",size=17,style="B")
        pdf.cell(w=100,h=40,txt="period",border=1)
        pdf.cell(w=150,h=40,txt=the_bill.period,ln=1,border=1)

        pdf.cell(w=100,h=40,txt=flatemate1.name,border=1)
        pdf.cell(w=150,h=40,txt=str(flatemate1.pays(flatemate2,the_bill)),border=1,ln=1)

        pdf.cell(w=100,h=40,txt=flatemate2.name,border=1)
        pdf.cell(w=150,h=40,txt=str(flatemate2.pays(flatemate1,the_bill)),border=1,ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)

amount=eval(input("Hey user , Enter the amount you need to split example 240 - "))
period=input("Enter the period of the bill exaple jan 2022 - ")
person1=input("Enter the name of the flatemate example vagish - ")
person2=input("Enter the name of the flatemate exaple naveen karthi - ")
no_of_days_of_person1=eval(input(f"Enter the number of days of {person1} - "))
no_of_days_of_person2=eval(input(f"Enter the number of days of {person2} - "))


the_bill=bill(amount=amount,period=period)


person_1=flatmate(name=person1,days_in_house=no_of_days_of_person1)
person_2=flatmate(name=person2,days_in_house=no_of_days_of_person2)



pfd=pfdGenerator("report.pdf")
pfd.generate(person_1,person_2,the_bill)










from fpdf import FPDF
import webbrowser

class bill():
    def __init__(self,amount,period):

        """object that contain data about the bill that is the period and amount of bill"""

        self.amount=amount
        self.period=period

class flatmate():
    def __init__(self,name,days_in_house):

        """Object that contain data about the name and number of days that the person stayed in the flat"""

        self.name=name
        self.days_in_house=days_in_house

    
    def pays(self,flatmatePerson,the_bill):
        weight=self.days_in_house/(self.days_in_house+flatmatePerson.days_in_house)
        to_pay=the_bill.amount*weight
        return to_pay

    
class pfdGenerator():
    def __init__(self,filename):
        self.filename=filename

        """This class is used to generate pdf by using the flatemates data"""

    def generate(self,flatemate1,flatemate2,the_bill):
        pdf=FPDF(orientation="p",unit="pt",format="A4")
        pdf.add_page()
        pdf.set_font(family="Times",size=24,style="B")
        pdf.cell(w=0,h=80,txt="Flatemate Bill",border=1,align="C",ln=1)
        pdf.set_font(family="Times",size=17,style="B")
        pdf.cell(w=100,h=40,txt="period",border=1)
        pdf.cell(w=150,h=40,txt=the_bill.period,ln=1,border=1)

        pdf.cell(w=100,h=40,txt=flatemate1.name,border=1)
        pdf.cell(w=150,h=40,txt=str(flatemate1.pays(flatemate2,the_bill)),border=1,ln=1)

        pdf.cell(w=100,h=40,txt=flatemate2.name,border=1)
        pdf.cell(w=150,h=40,txt=str(flatemate2.pays(flatemate1,the_bill)),border=1,ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)

amount=eval(input("Hey user , Enter the amount you need to split example 240 - "))
period=input("Enter the period of the bill exaple jan 2022 - ")
person1=input("Enter the name of the flatemate example vagish - ")
person2=input("Enter the name of the flatemate exaple naveen karthi - ")
no_of_days_of_person1=eval(input(f"Enter the number of days of {person1} - "))
no_of_days_of_person2=eval(input(f"Enter the number of days of {person2} - "))


the_bill=bill(amount=amount,period=period)


person_1=flatmate(name=person1,days_in_house=no_of_days_of_person1)
person_2=flatmate(name=person2,days_in_house=no_of_days_of_person2)



pfd=pfdGenerator("report.pdf")
pfd.generate(person_1,person_2,the_bill)











# class bill():
#     def __init__(self,amount,period):
#         self.amount=amount
#         self.period=period


# class flatmates():
#     def __init__(self,days_in_house):
#         self.days_in_house=days_in_house

#     def pays(self,flatemate,the_bill):
#         weight=self.days_in_house/(self.days_in_house+flatemate.days_in_house)
#         to_pay=the_bill.amount*weight
#         return to_pay

# bill=bill(amount=120,period="June 20")

# mary=flatmates(30)
# vagish=flatmates(10)

# print(mary.pays(flatemate=vagish,the_bill=bill))
# print(vagish.pays(flatemate=mary,the_bill=bill))




