#Michael Harris and John Mathews
#Machine Perfromance | CPSC 4240

#import libraries
import psutil
import platform

#mainMenu(): Display a main menu to the user to navigate program
def mainMenu():
    
    #prompt user
    print("Welcome to Machine Performance for Ubuntu Linux!")
    print("Select an option to continue:")

    #menu choices
    print("1) System Hardware Information")
    print("2) System Performance")
    print("4) System Energy Usage")
    print("5) Current Processes")
    print("6) Network Information")
    print("7) Quit Program")

    #prompt user input
    userChoice = input("Enter a menu option (1-7): ")

    if userChoice == "1":
        hardwareInfo()
        pass
    elif userChoice == "2":

        pass
    elif userChoice == "3":

        pass
    elif userChoice == "4":

        pass
    elif userChoice == "5":
        processInfo()
        pass
    elif userChoice == "6":

        pass
    elif userChoice == "7":

        exit()
    else:

        print("Invalid choice. Please enter a menu option again.")

    #call mainMenu() to continue to show options
    mainMenu()

#hardwareInfo(): 
def hardwareInfo():


    #print hardware information
    print("CPU: " + platform.processor())
    print("CPU Cores: " + str(psutil.cpu_count(logical = False)) + " physical, " + str(psutil.cpu_count()) + " total")
    print("RAM: " + str(psutil.virtual_memory().total / 1024 / 1024) + " MB")
    print("Swap: " + str(psutil.swap_memory().total / 1024 / 1024) + " MB")
    print("Disk Usage: " + str(psutil.disk_usage('/').used / 1024 / 1024) + " MB used out of " + str(psutil.disk_usage('/').total / 1024 / 1024) + " MB")

    #print battery life if the system is a laptop
    if psutil.sensors_battery() is not None:
        print("Battery: " + str(psutil.sensors_battery().percent) + "% (" + ("charging" if psutil.sensors_battery().power_plugged else "discharging") + ")")


def systemPerformance():

    pass  

def processInfo():
    print( )
    print("Process Information Menu:")
    print("Select an option to continue:")

    #menu choices
    print("1) Show Current Process IDs")
    print("2) Show information about a specific PID")
    print("3) Show children processes of a specific PID")
    print("4) Show parent processes of a specific PID")
    print("5) Show current status of a specific PID")
    print("10) Quit Program")

    #prompt user input
    userChoice = input("Enter a menu option (1-7): ")
    if userChoice == "1":
        print( )
        print("Current Processes:")
        print(str(psutil.pids()))
        print( )
        pass
    elif userChoice == "2":
        print( )
        print("Current Processes:")
        print(str(psutil.pids()))
        print( )
        userPID = input("Enter the PID to search for: ")
        print(str(psutil.Process(int(userPID))))
        pass
    elif userChoice == "3":
        print( )
        print("Current Processes:")
        print(str(psutil.pids()))
        print( )
        userPID = input("Enter the PID to search for children: ")
        p = psutil.Process(int(userPID))
        print(str(p.children(recursive = True)))
        pass
    elif userChoice == "4":
        print( )
        print("Current Processes:")
        print(str(psutil.pids()))
        print( )
        userPID = input("Enter the PID to search for parents: ")
        p = psutil.Process(int(userPID))
        print(str(p.parents()))
        pass
    elif userChoice == "5":
        print( )
        print("Current Processes:")
        print(str(psutil.pids()))
        print( )
        userPID = input("Enter the PID to search for status:")
        print(str(userPID.status()))
        pass
    elif userChoice == "6":

        pass
    elif userChoice == "10":
        exit()
    else:
        print("Invalid choice. Please enter a menu option again.")

    processInfo()

    pass
    

#call mainMenu() to start program
mainMenu()
    

