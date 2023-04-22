#Michael Harris and John Mathews
#Machine Perfromance | CPSC 4240

#Import Libraries
import psutil
import platform
import time


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
        systemPerformance()
    
    elif userChoice == "3":
        pass
        
    elif userChoice == "4":
        processInfo()

    elif userChoice == "5":
        networkInfo()

    elif userChoice == "6":
        exit()

    else:
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

#systemPerformance(): 
def systemPerformance():

    #Title
    print("\nSystem Performance Menu:")
    print("Select an option to continue:\n")

    #Menu choices
    print("1) Show CPU Performance")
    print("2) Show Memory Performance")
    print("3) Show Disk Performance")
    print("4) Show GPU Performance")
    print("5) Return to Main Menu")
    print("6) Quit Program\n")

    #Prompt user input
    userChoice = input("Enter a menu option (1-6): ")

    if userChoice == "1":

        #CPU Usage - util, speed, num processes, threads, uptime, caches
        print("\n CPU Utilization: " + str(psutil.cpu_percent()) + "%")
        ghz = psutil.cpu_freq().current / 1000
        print("\n CPU Speed: {:.2f}".format(ghz) + " GHz")
        print("\n Number of Processes Running: " + str(len(psutil.pids())))
        print("\n Number of Threads: " + str(psutil.Process().num_threads()))
        print("\n System Uptime: " + str(psutil.boot_time()) + "seconds")
        print("\n System Cache: " + str(psutil.disk_usage('/').percent))

        #prompt user
        print("\nTo see 15 second CPU Utilization Graph enter g. To go to System Performance menu, enter any other key.\n")

        #Utilization Graph
        if input() == "g":
            cpuUtilGraph()


    elif userChoice == "2":
        
        
        #Memory - in use, speed, committed, cached
        print("\nCurrent Memory(RAM) Usage: {:.2f} GB".format(psutil.virtual_memory().used / 1024 / 1024 / 1024))
        print("\nTotal Memory(RAM): {:.2f} GB".format(psutil.virtual_memory().total / 1024 / 1024 / 1024))
        print("\nCommitted Memory(RAM): {:.2f} GB".format(psutil.virtual_memory().percent / 100 * psutil.virtual_memory().total / 1024 / 1024 / 1024))
        print("\nCached Memory(RAM): {:.2f} GB".format(psutil.virtual_memory().cached / 1024 / 1024 / 1024))

        #Enable Memory Usage graph
        print("\nTo see 15 second RAM Utilization Graph enter g. To go to System Performance menu, enter any other key.\n")

        #Utilization Graph
        if input() == "g":
            memoryUtilGraph()
        pass
        
    elif userChoice == "3":
        
        #Disk - active time, avg response time, read speed, write speed, capacity
        print("Disk Active Time: {}%".format(psutil.disk_io_counters().busy_time))
        print("Average Response Time: {} ms".format(psutil.disk_io_counters().average_time))
        print("Read Speed: {:.2f} GB/s".format(psutil.disk_io_counters().read_bytes/1024/1024/1024))
        print("Write Speed: {:.2f} GB/s".format(psutil.disk_io_counters().write_bytes/1024/1024/1024))
        print("Disk Capacity: {:.2f} GB".format(psutil.disk_usage('/').total/1024/1024/1024))
        print("Number of Partitions: ", len(psutil.disk_partitions()))

        #Enable active time graph
        
        pass
        
    elif userChoice == "4":
        
        #GPU - utilization, GPU mem

        #Enable 3D graph?
        
        pass
        
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
        systemPerformance()

def cpuUtilGraph():

        #local variables
        interval = 1
        points = 20
        util = []
        x = "Time (seconds)"
        y = "CPU Utilization (%)"

        # Loop indefinitely
        for i in range(0,15):

            #get CPU Util & add
            cpuPercent = psutil.cpu_percent()
            util.append(cpuPercent)

            #remove oldest value when exceeding axis value
            if len(util) > points:
                util.pop(0)

            #set up the bar chart
            numChars = [int(util / 5) for util in util]
            rows = zip(*[" " * (10 - n) + "*" * n for n in numChars])
            chart = "\n".join(["".join(row) for row in rows])

            #print & wait
            chart = f"{y}\n{chart}\n{x}\n"
            print(f"{chart}") 
            time.sleep(interval)

        systemPerformance()

def memoryUtilGraph():
        
        #local variables
        interval = 1
        points = 20
        util = []
        x = "Time (seconds)"
        y = "Memory Utilization (%)"

        # Loop indefinitely
        for i in range(0,15):

            #get CPU Util & add
            memPercent = psutil.virtual_memory().percent
            util.append(memPercent)

            #remove oldest value when exceeding axis value
            if len(util) > points:
                util.pop(0)

            #set up the bar chart
            numChars = [int(util / 5) for util in util]
            rows = zip(*[" " * (10 - n) + "*" * n for n in numChars])
            chart = "\n".join(["".join(row) for row in rows])

            #print & wait
            chart = f"{y}\n{chart}\n{x}\n"
            print(f"{chart}") 
            time.sleep(interval)

        systemPerformance()


#systemEnergy():
def systemEnergy():



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

#networkInfo():
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

#netowrkConnections():
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