import json
class cisco:
    '''An object used to keep track of Cisco IOS commands'''
    def __init__(self, keywords):
        self.keywords = keywords
        self.ip_addr = ''
        self.subnet = ''
        self.vlan_name = ''
        self.interface_id = ''
        self.vlan_id = 1
        self.i = ''
        self.vlan_active = ''
        self.sw_mode = ''
        self.interface = ''

        
        self.cisco_dict = {} # <******** This is the root dictionary ***********
        self.vlan_dict = {} # Vlan Dictionary
        self.sw_mode_dict = {} # Switchport Mode dictionary
        self.interface_dict = {} # Interface dictionary
        
    def vlan(self):
        '''
        This defines the vlan creation module
        First while statement checks to see if Vlan ID falls within bounds
        If statement asks for Vlan name
        '''
        
        while self.i != 'r':
            try:
                self.vlan_id = int(input("Enter the Vlan ID\n"))
                if self.vlan_id > 1 and self.vlan_id < 999:
                    self.i = 'r'
                    self.vlan_active = True
                else:
                    raise TypeError("Invalid entry. Vlan must be an integer.")
            # except TypeError:
            #     self.i = ''
            #     print("TYPE ERROR. Are you assigning values correctly?")
            #     self.vlan_id = int(input("What VLAN will you use? (enter ID) \n"))
            #     continue
            except:
                print("Error. Unhandled exception in vlan module.")
            #     print("Error at vlan_id value entry.")
            try:
                self.vlan_name = input("What is the Vlan name? \n")
                if isinstance(self.vlan_name, str):
                    pass
                else:
                    raise ValueError
            except :
                print("Error. Unhandled exception in vlan module.")
                print("Error at vlan_name value entry.")
 
            
    def port_range(self, interface_sgfa, int_range=1): 
        ''' 
        Second parameter is used to take in whether the user wants
        Gigabit, FastEthernet, or Serial interface types

        Third Parameter takes the number of interfaces that need to be configured

        This module takes in a range of interfaces and saves the proper commands
        to a dictionary
        '''
        try:
            for i in range(self.int_range):
                if interface_sgfa.lower() in ['S', 'S0/0', 'S0', 'Serial', 'ser']:
                    i -= 1
                    self.command[i] = f"interface range serial0/{i} - {int_range}"
                    self.interface_dict["Interface range and type" + i] = (f"interface range serial0/{i} - {int_range}")
                elif interface_sgfa.lower() in ['f', 'fa', 'fast', 'fastethernet', 'fa0', 'fa0/0', 'fa0/0.0']:
                    self.interface_dict["Interface range and type" + i] = f"interface range FastEthernet0/{i} - {int_range}"
                elif interface_sgfa.lower() in ['g', 'gi', 'giga', 'gigabit', 'g0', 'g0/0', 'g0/0.0']:
                    self.interface_dict["Interface range and type" + i] = f"interface range GigabitEthernet0/{i} - {int_range}"    
        except ValueError:
            print("ERROR. Invalid range.")
        finally:
            print("Range commands saved.")



    def output(self):
        '''
        This module prints and outputs all of the 
        commands from the instance to a file and the shell
        '''
        if self.vlan_active == True:
            print(f"vlan {self.vlan_id}")
            print(f"name {self.vlan_name}")
            # print(f"int {self.interface_id}")
            self.vlan_dict["vlan_id"] = f"vlan {self.vlan_id}"
            self.vlan_dict["name"] = f"name {self.vlan_name}"
            # self.vlan_dict["interface"] = f"int {self.interface_id}"

            self.cisco_dict["vlan commands"] = self.vlan_dict 

        if self.sw_mode == True :
            print(f"switchport mode {self.sw_mode}") # Write a line to capture if interface is trunk or access port
            print(f"switchport access vlan {self.vlan_id}")

            self.sw_mode_dict["Switchport mode"] = (f"switchport mode {self.sw_mode}")
            if self.vlan_active == True:
                self.sw_mode_dict["Switchport mode"] = (f"switchport access vlan {self.vlan_id}")
                self.cisco_dict["Switchport Modes"] = self.sw_mode_dict
        
        if self.interface_id == True: 
            '''Checks to see if Interface 
                commands were entered and saves to a dictionary
            '''
            for i in range(int_range):
                self.cisco_dict["Int Range" + i] = self.interface_dict["Interface range and type" + i]


            print("exit")
        return self.cisco_dict

# ------------------------------ CODE ABYSS --------------------------------------- #
        # try:
        #     self.interface_id = input("Enter the Interface number (g0/0, fa0/0, etc.)\n")
        #     if isinstance(self.interface_id, str):
        #         pass
        #     else:
        #         raise ValueError
        # except ValueError:
        #     print("Error, value entered is not a string.\n"
        #             "remember to include the Gigabit or FastEthernet\n"
        #             "interface portion of the str.")
            