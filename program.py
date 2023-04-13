#Michael Harris and John Mathews
#Machine Perfromance | CPSC 4240

#Import Libraries
import psutil
import platform

#mainMenu(): Display a main menu to the user to navigate program
def mainMenu():

    #Title
    print("\nWelcome to Machine Performance for Ubuntu Linux!")
    print("Select an option to continue:\n")

    #Menu choices
    print("1) System Hardware Information")
    print("2) System Performance")
    print("3) System Energy Usage")
    print("4) Current Processes")
    print("5) Network Information")
    print("6) Quit Program\n")

    #Prompt user input
    userChoice = input("Enter a menu option (1-6): ")

    #Logic ladder for menu options
    if userChoice == "1":
        hardwareInfo()

    elif userChoice == "2":
        pass

    elif userChoice == "3":
        pass
        
    elif userChoice == "4":
        processInfo()

    elif userChoice == "5":
        networkInfo()

    elif userChoice == "6":
        #Exit the program
        exit()

    else:
        #Error Handler
        print("Invalid choice. Please enter a menu option again.")

    #call mainMenu() to continue to show options
    mainMenu()

#hardwareInfo(): Displays basic hardware components of system
def hardwareInfo():

    #print hardware information
    print("\nCPU: " + platform.processor())
    print("CPU Cores: " + str(psutil.cpu_count(logical = False)) + " physical, " + str(psutil.cpu_count()) + " total")
    print("RAM: " + str(psutil.virtual_memory().total / 1024 / 1024) + " MB")
    print("Swap: " + str(psutil.swap_memory().total / 1024 / 1024) + " MB")
    print("Disk Usage: " + str(psutil.disk_usage('/').used / 1024 / 1024) + " MB used out of " + str(psutil.disk_usage('/').total / 1024 / 1024) + " MB")
    print("Boot Time: " + str(psutil.boot_time()))
    print("Sensor Temperatures: " + str(psutil.sensors_temperatures()))
    print("Sensor Fans: " + str(psutil.sensors_fans()))
    print("Sensor Battery: " + str(psutil.sensors_battery()))

    #print battery life if the system is a laptop
    if psutil.sensors_battery() is not None:
        print("Battery: " + str(psutil.sensors_battery().percent) + "% (" + ("charging" if psutil.sensors_battery().power_plugged else "discharging") + ")")

    print("\n")


def systemPerformance():

    pass

#processInfo(): Function containing menu logic and calculations involving the process option
def processInfo():

    #Title
    print("\nCurrent Process Information Menu:")
    print("Select an option to continue:\n")

    #Menu choices
    print("1) Show Current Process IDs")
    print("2) Show general information of a specific process")
    print("3) Show children processes of a specific process")
    print("4) Show parent processes of a specific process")
    print("5) Show current status of a specific process")
    print("6) Show CPU time of a specific process")
    print("7) Show memory information of a specific process")
    print("8) Show environment variables of a specific process")
    print("9) Open Process Control Menu")
    print("10) Return to Main Menu")
    print("11) Quit Program\n")

    #Prompt user input
    userChoice = input("Enter a menu option (1-11): ")


    if userChoice == "1":
        #Show current processes and information about them
        print("\nCurrent Processes:")
        print(str(psutil.pids()))
        print(str(psutil.test()))
        
    elif userChoice == "2":
        #Show current processes
        print("\nCurrent Processes:")
        print(str(psutil.pids()) + "\n")
        #Get what PID user chooses
        userPID = input("Enter the PID to search for: ")
        p = psutil.Process(int(userPID))
        #Call specific functions and state information
        print("Process " + userPID + "'s General Information: " +  str(psutil.Process(int(userPID))))
        print("Process " + userPID + "'s Input/Output Counters: " +  str(p.io_counters()))
        print("Process " + userPID + "'s Connections: " +  str(p.connections(kind='tcp')))
        print("Process " + userPID + "'s Threads: " +  str(p.threads()))
        
    elif userChoice == "3":
        #Show current processes
        print("\nCurrent Processes:")
        print(str(psutil.pids()) + "\n")
        #Get what PID user chooses
        userPID = input("Enter the PID to search for children: ")
        p = psutil.Process(int(userPID))
        #Call specific functions and state information
        print("Process " + userPID + "'s Children: " + str(p.children(recursive = True)) + "\n")
        
    elif userChoice == "4":
        #Show current processes
        print("\nCurrent Processes:")
        print(str(psutil.pids()) + "\n")
        #Get what PID user chooses
        userPID = input("Enter the PID to search for parents: ")
        p = psutil.Process(int(userPID))
        #Call specific functions and state information
        print("Process " + userPID + "'s Parents: " + str(p.parents()))
        
    elif userChoice == "5":
        #Show current processes
        print("\nCurrent Processes:")
        print(str(psutil.pids()) + "\n")
        #Get what PID user chooses
        userPID = input("Enter the PID to search for status: ")
        p = psutil.Process(int(userPID))
        #Call specific functions and state information
        print("Process " + userPID + "'s Status: " + str(p.status()))
        
    elif userChoice == "6":
        #Show current processes
        print("\nCurrent Processes:")
        print(str(psutil.pids()) + "\n")
        #Get what PID user chooses
        userPID = input("Enter the PID to search for CPU time: ")
        p = psutil.Process(int(userPID))
        #Call specific functions and state information
        print("Process " + userPID + "'s CPU Time: " + str(p.cpu_times()))
        
    elif userChoice == "7":
        #Show current processes
        print("\nCurrent Processes:")
        print(str(psutil.pids()) + "\n")
        #Get what PID user chooses
        userPID = input("Enter the PID to search for memory information: ")
        p = psutil.Process(int(userPID))
        #Call specific functions and state information
        print("Process " + userPID + "'s Memory Info: " + str(p.memory_info()))
        print("Process " + userPID + "'s Memory Maps: " + str(p.memory_maps()))
        
    elif userChoice == "8":
        #Show current processes
        print("\nCurrent Processes:")
        print(str(psutil.pids()) + "\n")
        #Get what PID user chooses
        userPID = input("Enter the PID to search for environment variables: ")
        p = psutil.Process(int(userPID))
        #Call specific functions and state information
        print("Process " + userPID + "'s Environment Variables: " + str(p.environ()) + "\n")
        
    elif userChoice == "9":
        #Call to function that handles process control
        processControl()
        
    elif userChoice == "10":
        #Call to function that handles the main menu
        mainMenu()
        
    elif userChoice == "11":
        #Call to exit program
        exit()
    else:
        #Error handler
        print("Invalid choice. Please enter a menu option again.")

    if(userChoice != 9):
        processInfo()

    

#processControl(): Helper function that deals with the process control functionality and logic
def processControl():

    #Title
    print("\nProcess Control Menu:")
    print("Select an option to continue:\n")

    #Menu choices
    print("1) Resume")
    print("2) Suspend")
    print("3) Terminate")
    print("4) Kill")
    print("5) Force Wait")
    print("6) Return to Process Menu")

    #Prompt for user input
    userChoice = input("Enter a menu option (1-6): ")

    if userChoice == "1":
        #Show current processes
        print("\nCurrent Processes:")
        print(str(psutil.pids()) + "\n")
        #Get what PID user chooses
        userPID = input("Enter the PID to resume: ")
        p = psutil.Process(int(userPID))
        #Call specific function and state what has happened
        p.resume()
        print("Process " + userPID + " has been resumed.")
        
    elif userChoice == "2":
        #Show current processes
        print("\nCurrent Processes:")
        print(str(psutil.pids()) + "\n")
        #Get what PID user chooses
        userPID = input("Enter the PID to suspend: ")
        p = psutil.Process(int(userPID))
        #Call specific function and state what has happened
        p.suspend()
        print("Process " + userPID + " has been suspended.")
        
    elif userChoice == "3":
        #Show current processes
        print("\nCurrent Processes:")
        print(str(psutil.pids()) + "\n")
        #Get what PID user chooses
        userPID = input("Enter the PID to terminate: ")
        p = psutil.Process(int(userPID))
        #Call specific function and state what has happened
        p.terminate()
        print("Process " + userPID + " has been terminated.")
        
    elif userChoice == "4":
        #Show current processes
        print("\nCurrent Processes:")
        print(str(psutil.pids()) + "\n")
        #Get what PID user chooses
        userPID = input("Enter the PID to kill: ")
        p = psutil.Process(int(userPID))
        #Call specific function and state what has happened
        p.kill()
        print("Process " + userPID + " has been kill.")
        
    elif userChoice == "5":
        #Show current processes
        print("\nCurrent Processes:")
        print(str(psutil.pids()) + "\n")
        #Get what PID user chooses and how much time to wait
        userPID = input("Enter the PID to force wait: ")
        p = psutil.Process(int(userPID))
        time = input("Enter the amount of time to force wait: ")
        #Call specific function and state what has happened
        p.wait(timeout = int(time))
        print("Process " + userPID + " has been forced to wait.")
        
    elif userChoice == "6":
        #Call back to process information function
        processInfo()
        
    else:
        #Error handler
        print("Invalid choice. Please enter a menu option again.")

    #Repeat until user selects to return to previous menu
    processControl()

def networkInfo():
     #Title
    print("\nNetwork Information Menu:")
    print("Select an option to continue:\n")

    #Menu choices
    print("1) Show Network Input/Output Counters")
    print("2) Show Network Connections of a specified type")
    print("3) Show Network Addresses")
    print("4) Show Network Stats")
    print("5) Return to Main Menu")
    print("6) Quit Program\n")

    #Prompt user input
    userChoice = input("Enter a menu option (1-6): ")


    if userChoice == "1":
        print(str(psutil.net_io_counters(pernic=True)))
        
    elif userChoice == "2":
        networkConnections()
        
    elif userChoice == "3":
        print(str(psutil.net_if_addrs()))
        
    elif userChoice == "4":
        print(str(psutil.net_if_stats()))
        
    elif userChoice == "5":
        #Call to function that handles the main menu
        mainMenu()
        
    elif userChoice == "6":
        #Call to exit program
        exit()
    else:
        #Error handler
        print("Invalid choice. Please enter a menu option again.")

    if(userChoice != 5):
        networkInfo()
    
def networkConnections():
     #Title
    print("\nConnection Types Menu:")
    print("Select a type to search for:\n")

    #Menu choices
    print("1) TCP Connections")
    print("2) UDP Connections")
    print("3) INET Connections")
    print("4) All Connections")
    print("5) Return to Network Menu")
    print("6) Quit Program\n")

    #Prompt user input
    userChoice = input("Enter a menu option (1-6): ")


    if userChoice == "1":
        print(str(psutil.net_connections(kind='tcp')))
        
    elif userChoice == "2":
        print(str(psutil.net_connections(kind='udp')))
        
    elif userChoice == "3":
        print(str(psutil.net_connections(kind='inet')))
        
    elif userChoice == "4":
        print(str(psutil.net_connections(kind='all')))
        
    elif userChoice == "5":
        #Call to function that handles the main menu
        networkInfo()
        
    elif userChoice == "6":
        #Call to exit program
        exit()
    else:
        #Error handler
        print("Invalid choice. Please enter a menu option again.")

    if(userChoice != 5):
        networkConnections()

#Call mainMenu() to start program
mainMenu()