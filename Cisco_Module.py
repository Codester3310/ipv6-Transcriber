import json
class cisco:
    '''An object used to keep track of ip addressing and commands'''
    def __init__(self):
        self.ip_addr = ''
        self.subnet = ''
        self.vlan_name = ''
        self.interface_id = ''
        self.vlan_id = 1
        self.i = ''
        self.interfacerange = {}
        
        
    def vlan(self, **vlan_id):
        '''
        This defines the vlan creation module
        First while statement checks to see if Vlan ID falls within bounds
        If statement asks for Vlan name
        '''
        
        while self.i != 'r':
            try:
                self.vlan_id = int(input("Enter the vlan id"))
                if self.vlan_id > 1 and self.vlan_id < 999:
                    self.i = 'r'
                    self.vlan = True
                else:
                    raise TypeError("Invalid entry. Vlan must be an integer.")
            except TypeError:
                vlan_id = int(input("What VLAN will you use?"))
            except:
                print("Error. Unhandled exception in vlan module.")
                print("Error at vlan_id value entry.")
            try:
                self.vlan_name == input("What is the Vlan name?")
                if isinstance(self.vlan_name, str):
                    pass
                else:
                    raise ValueError
            except :
                print("Error. Unhandled exception in vlan module.")
                print("Error at vlan_name value entry.")


    def output(self):
        '''
        This module prints and outputs all of the 
        commands from the instance to a file and the shell
        '''
        try:
            if vlan == True:
                print(f"vlan {self.vlan_id}")
                print(f"name {self.vlan_name}")
                print(f"int {self.interface_id}")

                
                try:
                    self.interface_id = input("Enter the Interface number (g0/0, fa0/0, etc.).")
                    if isinstance(self.interface_id, str):
                        pass
                    else:
                        raise ValueError
                except ValueError:
                    print("Error, value entered is not a string.\n"
                            "remember to include the Gigabit or FastEthernet\n"
                            "interface portion of the str.")
                    
                if self.sw_mode == True:
                    print(f"switchport mode {self.sw_mode}") # Write a line to capture if interface is trunk or access port
                    print(f"switchport access vlan {self.vlan_id}")
                
                else:
                    pass
            else:
                raise ValueError("Missing data from printed statement.")
        except ValueError:
            if self.vlan == False:
                if vlan_id == 1:
                        self.vlan_id = int(input("Enter your VLAN ID.\n"))
                elif self.vlan_name == False:
                    self.vlan_name = input("Enter your vlan name.\n")
            else:
                self.interface_id = False
        finally:
            print("exit")
            
        def port_range(self, interface_sgfa, int_range='0/0 - 5'): 
            ''' 
            Second parameter is used to take in whether the user wants
            Gigabit, FastEthernet, or Serial interface types

            This module takes in a range of interfaces and saves the proper commands
            to a dictionary
            '''
            try:
                for i in range(self.int_range):
                    if interface_sgfa.lower() in ['S', 'S0/0', 'S0', 'Serial', 'ser']:
                        i -= 1
                        self.command[i] = f"interface range serial0/{i} - {range}"
                        self.interface_dictionary.append(f"interface range serial0/{i} - {range}")
                    elif interface_sgfa.lower() in ['f', 'fa', 'fast', 'fastethernet', 'fa0', 'fa0/0', 'fa0/0.0']:
                        self.command[i] = f"interface range FastEthernet0/{i} - {range}"
                    elif interface_sgfa.lower() in ['g', 'gi', 'giga', 'gigabit', 'g0', 'g0/0', 'g0/0.0']:
                        self.command[i] = f"interface range GigabitEthernet0/{i} - {range}"    
            except ValueError:
                print("ERROR. Invalid range.")
            finally:
                print("Range commands saved.")



