class Car:
    def __init__(self, license, model, color) -> None:
        self.license=license
        self.model=model
        self.color=color
        pass
    def __repr__(self) -> str:
        return f"{self.license}, {self.model}, {self.color}"

class Garage:
    def __init__(self) -> None:
        self.car_added=[] #license, model, color
        self.spot=10
        self.car_info={} #license, model, color, ticket
        pass

    def spots_available(self):
        return f"Total Spots Available:{self.spot}"
        # return self.spot
    
    def add_car_to_garage(self, car):
        # user_data=car.split(', ')
        self.spot_name=['A1', 'B1','C1','D1','E1','F1','G1','H1','I1','J1']
        if self.spot>0:
            user_data=str(car).split(', ')
            self.spot-=1
            self.car_added.append(user_data)
            self.car_info={'Ticket':[],'License':[],'Model':[],'Color':[]}
            ticket=""

            for i, val in enumerate(self.car_added):
                ticket=self.spot_name[i]+val[0]
                self.car_info['Ticket'].append(ticket)
                self.car_info['License'].append(val[0])
                self.car_info['Model'].append(val[1])
                self.car_info['Color'].append(val[2])
            print(f"Successfully parked! Yout ticket:{ticket}")
            print('\n')
        else:
            print("No spot available")

    def unpark(self,ticket,hours):
        past_spot_len=len(self.car_info['Ticket'])

        if ticket not in self.car_info['Ticket']:
            print('No car found')
            return
        else:
            for i, val in enumerate(self.car_info['Ticket']):
                if val==ticket:
                    print(f"Your license no:{self.car_info['License'][i]}")
                    print(f"Your car model is:{self.car_info['Model'][i]}")
                    print(f"Your car colour is:{self.car_info['Color'][i]}")
                    print('********************************')
                    removed_car_index=i
                    self.car_info['License'].pop(i)
                    self.car_info['Model'].pop(i)
                    self.car_info['Color'].pop(i)
                    self.car_info['Ticket'].pop(i)
                    self.spot+=1
        if hours>20:
            print(f"Total Bill=${hours*5+100}")
            print('\n')
        else:
            print(f"Total Bill = ${hours*5}")

    def total_cars_in_garage(self):
        for i in self.car_info.items():
            print(i)



        
        
# car1=Car('123az','tesla-v7','red')
# car2=Car('54lll','bmw i=8','black')
# car3=Car('98745','toyota','blue')
# car4=Car('9999','bmw i=8','green')

# my_garage=Garage()
# my_garage.add_car_to_garage(car1)
# my_garage.add_car_to_garage(car2)
# my_garage.add_car_to_garage(car3)
# my_garage.add_car_to_garage(car4)
# my_garage.total_cars_in_garage()
# my_garage.unpark('A1123az',21)
# my_garage.unpark('B154lll',10)
# my_garage.total_cars_in_garage()

my_garage = Garage()

print("****************WELCOME TO OUR PARKING SYSTEM**************")

while True:
    print("What do you want ? ")
    print("1. Park your Car \n2. Check Available Space \n3. Unpark Your Car \n4. Total Cars in Garage \n5. Exit")
    user_choice = int(input("Enter you choice : "))
    if user_choice==1:
        car_license = input("Enter your car license : ")
        car_model = input("Enter your car model : ")
        car_color = input("Enter your car color : ")
        user_car = Car(car_license, car_model, car_color) # Car class object
        my_garage.add_car_to_garage(user_car)
        print()

    elif user_choice==2:
        print(my_garage.spots_available())
        print() 

    elif user_choice==3:
        ticket = input("Enter your ticket number : ")
        hours  = int(input("Enter hours : "))
        if my_garage.spot == 10:
            print('There is no car in parking')
            continue
        else:
            my_garage.unpark(ticket, hours)
        print()
    elif user_choice==4:
        print(my_garage.total_cars_in_garage())
    elif user_choice==5:
        break
    else:
        print("Invalid Choice")
    


    '''
    class Car:
    def __init__(self, license, model, color):
        self.license = license
        self.model = model
        self.color = color
    def __repr__(self):
        return f"{self.license},{self.model},{self.color}"

class Garage:
    def __init__(self):
        self.car_added = []
        self.spot = 10
        self.car_infos = {}
    
    def spots_available(self):
        return f"Total Spots Available {self.spot}"
    
    def add_car_to_garage(self, car):
# A1 : {}
        self.spot_name = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'J1']
        if self.spot > 0:
            user_data = str(car).split(',')
            self.spot -=1
            self.car_added.append(user_data) 
            self.car_infos = {'Tickets' : [], 'License' : [], 'Model' : [],'Color' : []}
            ticket = ""
            
            for i, val in enumerate(self.car_added): # [[], [], [], [], []]
                ticket = self.spot_name[i] + val[0]
                self.car_infos['Tickets'].append(ticket)
                self.car_infos['License'].append(val[0])
                self.car_infos['Model'].append(val[1])
                self.car_infos['Color'].append(val[2])
            print(f"Successfully Parked!!! YOUR TICKET {ticket}")
        else:
            print("NO SPOTS AVAILABLE!!!!!!")
    
    def unpark(self, ticket, hours):
        if ticket not in self.car_infos['Tickets']: # security check purpose O(N)
            print("NO CAR FOUND!!!!!!!")
            return
        else:
            for i, val in enumerate(self.car_infos['Tickets']): #O(N)
                if val == ticket:
                    print(i)
                    print(f"YOUR LICENSE IS {self.car_infos['License'][i]}")
                    print(f"YOUR MODEL IS {self.car_infos['Model'][i]}")
                    print(f"YOUR COLOR IS {self.car_infos['Color'][i]}")
                    self.car_infos['License'].pop(i)
                    self.car_infos['Model'].pop(i)
                    self.car_infos['Color'].pop(i)
                    self.car_infos['Tickets'].pop(i)
                    self.spot += 1
        if hours > 30:
            print(f"Total Bill = ${hours*5 + 100}")
        else:
            print(f"Total Bill = ${hours*5}")
    def total_cars_in_garage(self):
        for i in self.car_infos.items():
            print(i)
    
my_garage = Garage()

print("****************WELCOME TO OUR PARKING SYSTEM**************")

while True:
    print("What do you want ? ")
    print("1. Park your Car \n2. Check Available Space \n3. Unpark Your Car \n4. Total Cars in Garage")
    user_choice = int(input("Enter you choice : "))
    if user_choice == 1:
        car_license = input("Enter your car license : ")
        car_model = input("Enter your car model : ")
        car_color = input("Enter your car color : ")
        user_car = Car(car_license, car_model, car_color) # Car class object
        my_garage.add_car_to_garage(user_car)
        print()
    elif user_choice == 2:
        print(my_garage.spots_available())
        print()
    elif user_choice == 3:
        ticket = input("Enter your ticket number : ")
        hours  = int(input("Enter hours : "))
        if my_garage.spot == 10:
            continue
        else:
            my_garage.unpark(ticket, hours)
        print()
    elif user_choice == 4:
        my_garage.total_cars_in_garage()
    else:
        break
    '''

    
    


        




   
    
         
    
    
    
         

