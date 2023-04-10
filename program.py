#Michael Harris and John Mathews
#Machine Perfromance | CPSC 4240

#import libraries
import psutil

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
    elif userChoice == "2":

        pass
    elif userChoice == "3":

        pass
    elif userChoice == "4":

        pass
    elif userChoice == "5":

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
    print("CPU: " + psutil.cpu_info().brand)
    print("CPU Cores: " + str(psutil.cpu_count(logical = False)) + " physical, " + str(psutil.cpu_count()) + " total")
    print("RAM: " + str(psutil.virtual_memory().total / 1024 / 1024) + " MB")
    print("Swap: " + str(psutil.swap_memory().total / 1024 / 1024) + " MB")
    print("Disk Usage: " + str(psutil.disk_usage('/').used / 1024 / 1024) + " MB used out of " + str(psutil.disk_usage('/').total / 1024 / 1024) + " MB")
    print("Battery: " + str(psutil.sensors_battery().percent) + "% (" + ("charging" if psutil.sensors_battery().power_plugged else "discharging") + ")")
    #print("Network Usage: " + str(psutil.net_io_counters().bytes_sent / 1024 / 1024) + " MB sent, " + str(psutil.net_io_counters().bytes_recv / 1024 / 1024) + " MB received")


def systemPerformance():

    pass  

#call mainMenu() to start program
mainMenu()
    

