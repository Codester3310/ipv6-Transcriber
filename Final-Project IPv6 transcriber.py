import json, math, Cisco_Module, re
# Save key names to key values in dictionary

    # Asks for string to be used in major portions of algorithm
# network_address = input("Please enter your Global Routing IP address (include colons).\n")
network_address = "2001:0451:0051" # Placeholder
host_segment = '0000:0000:0000:0000'
c = False
global_prefix_cider = ''
truncated_list = []
segments_dict = {}
command_list = ['Vlan', 'Range', 'Default Gateway', 'Quit']
_ = ''
# Determines notation and format of output


def ver_cid_variable_forager():      
    '''IMPORTANT-- this function grabs all variables required for CIDER and Verbose formats'''
    global v6_Seg_Count, subnet_address, host_estimate, total_estimate,host_distribute, ip_file_path, truncated_list, subnet_address             
    c = False
    manual_Even_Toggle = ["manually", "manual", "man", "m", "evenly", "even", "eve", "ev", "e"]
    while c == False:
    #   Asks for variables that determine range and loop iterations
        try: # Gets total estimate and handles value errors
            v6_Seg_Count = int(input("How many subnet segments do you want?\n"))
            if isinstance(v6_Seg_Count, int):

                host_estimate = int(input("How many hosts do you expect to use your network (total)?\n"))
                if isinstance(host_estimate, int):
                        
                    total_estimate = host_estimate + v6_Seg_Count
                    if not isinstance(total_estimate, int):
                        raise ValueError
                else:
                    raise ValueError
            else:
                raise ValueError 
        except ValueError:
            print("Invalid entry. Please enter an integer")
            continue

    # -----------------------------------------------------------

        try:        
            # Case variable to track how to calculate the print out formula
            host_distribute = input("Manually assign host count per segment or distrbute hosts evenly?\n")
            if isinstance(host_distribute, str) and host_distribute.lower() in manual_Even_Toggle:
                
                        # Asks for file path information
                ip_file_path = input(r"Enter your file name (path optional)." + "\n") 
                if isinstance(ip_file_path, str):
                    c = True
                else:
                    raise ValueError
            else:
                raise ValueError 
        except ValueError:
            print("Invalid entry. Please enter a string.")
            continue

    ''' subnet_address is the largest subnet addr defined. 
        Increment downwards till zero to use all subnets
        OR increment from zero till your index is greater than subnet_address
    '''
    subnet_address = (f"{v6_Seg_Count:04x}") 

def write_ipv6_to_json(segmentsW): # Write file function
    '''
    Writes data to a json file, adds a new line after every entry

    Args: 
        ip_file_path: The absolute or relative path the user set 
        (Global Variable needs to be defined before running this function)

        file_out_obj: the name of the .json file being written to
    '''

    with open( file=ip_file_path, # Opens file to write and Designates the writing filepath 
        mode='w') as file_out_obj: # file_out_obj is a placeholder variable
        json.dump(segmentsW, file_out_obj, indent=4)
        file_out_obj.write('\n')  # Add a newline after each entry
        # Still need to write function component that exports all data to save file


    # Defines CIDER conversion function
    
    pass

def format_verbose (): # Defines verbose conversion format
# this loop saves addresses to the segments dictionary
    ver_cid_variable_forager()
    for i in range(v6_Seg_Count):

        key = f"subnet_{i}".format(i+1)
        value = f"value_{i}".format(i+1)
        segments_dict[key] = value
    write_ipv6_to_json(segments_dict)
    pass


def format_cisco():
    keywords = []
    cisco_command_dict = {}
    interface_type = 'fa0/0'
    while True:
        try:
            user_input = (input("Input a command (ex. Vlan, range, q for quit)\n"))
            if isinstance(user_input, str): 
                keywords.append(user_input) # input Checker
                if user_input.lower() in ("q", "quit"):
                    break
                cisco = Cisco_Module.cisco(keywords) # Assigns the variable 'cisco' to an instance of the Cisco class
                if user_input.lower() in ['help', 'h']:
                    print(f"Commands include:\n{command_list}")
                
                    raise ValueError("Unknown Value error.")
            else:
                raise ValueError
        except ValueError:
            print("Error, bad keyword detected. Type Help for list of commands")
            continue
        try:
            routers = int(input("How many routers are you configuring?\n"))
            if isinstance(routers, int):
                    for iteration in range(routers):

                        '''Vlan keyword check. Runs Cisco_Module.vlan module'''
                        if "vlan" in keywords:
                            
                            # Requests Vlan ID from terminal
                            cisco_command_dict['vlan'+ iteration] = cisco.vlan()
                        
                        if "range" in keywords:
                            try:
                                interface_total = int(input("What is your port density (single integers 0 to 384)\n"))
                                if isinstance(interface_total, int):
                                    interface_type = input("What kind of port are you configuring? (Serial, Gigabit, FastEthernet)\n")
                                    cisco.port_range(interface_type, interface_total)

                                else:
                                    raise ValueError("Invalid entry. Enter the number of interfaces")
                            except ValueError:
                                continue


                # Defines Cisco conversion function. This runs a for loop to save ipv6 host addresses in a cisco router format
            else: raise ValueError
        except ValueError:
            print("Invalid value entered.") 
        finally:
            # Saves output
            cisco_command_dict["Vlan" + str(iteration)] = cisco.output()             
            return cisco_command_dict

def cisco_switch_commands():
    '''
    Generate cisco commands
    Pulls in Global IP addr, segment portion, and
    '''
    print("Enable\n")
    print("Configure Terminal\n")
    for i in v6_Seg_Count:
    # writes out ipv6 interface access and ip assignment commands 
        print(f"interface FastEthernet0/{range(i)}\n")
        print("ipv6 enable\n")
        print(f"ipv6 address {network_address}{subnet_address[i]}{address_prefix}")

def cisco_save(save_data, f):
    '''need to write this to be the final function that saves dictionary in cisco format
        to a dict and finishes by running write_ipv6_to_json() function.
    '''
    o = True
    while o == True:
        global ip_file_path
        try:
            if ip_file_path != '':
                if ip_file_path[-5:] !='.json': # Checks to see if entry has .json file extension
                    ip_file_path = f"{ip_file_path}.json" # adds .json if missing   
                with open( file=ip_file_path, # Opens file to write and Designates the writing filepath 
                    mode='a+') as f: # file_out_obj is a placeholder variable
                    json.dump(save_data, f, indent=4)
                    f.write('\n')  # Add a newline after each entry
                    o = False
            else:
                raise FileNotFoundError("File name blank")
        except FileNotFoundError:
            ip_file_path = "Untitled_Cisco_Commands.json"
            o = True
            continue
                # TODO write save file in txt format
            # save_data = Cisco_Module.cisco()
            # save_data[x].port_range(s, int(5))




def format_cider():
    '''
    CIDER path: writes output to .json in cider networking
    format. *NOTE* Zero suppression includes all leading zeros
            **Please chcek to see if your network configuration tool
            **or fixture uses the same or different trunkation format
            **before plug-and-playing .json file     
    '''
    address_prefix = prefix_length(total_estimate)
    seg0, seg1, seg2 = cider_slice() # Slices the global address into hextets   
    truncated_list = cider_trunc(seg0, seg1, seg2) # trunkates variables from leading zeros

    global_segment_compressed = concat_smash(truncated_list)
    cider_batch_addr_write(v6_Seg_Count, host_estimate)

def cider_slice():
    
    '''Variable for splitting the global address into
    substring variables

        Args:
            seg0 seg2: these strings are used to slice and hold
            the global IP address  
    '''
    seg0_0to3 = network_address[0:4]
    seg1_5to8= network_address[5:9]
    seg2_10to13 = network_address[10:14]
    
    return seg0_0to3, seg1_5to8, seg2_10to13

def cider_trunc(seg0, seg1, seg2):
    '''Look at the global address and the host segment
    and trunkate any segment that starts ends with a zero
    and has more than one zero in succession
    '''
    
    hextet_vars = [seg0, seg1, seg2] # Puts arguments into a list

    for i in range(len((hextet_vars))):
        # Check for at least two characters and two leading zeros
        if len(hextet_vars[i]) > 1 and hextet_vars[i].startswith('0'):  
            while len(hextet_vars[i]) > 1 and hextet_vars[i].startswith('0'):

                # Remove a single leading zero, stop if only one character remains
                hextet_vars[i] = hextet_vars[i][1:]  

    return hextet_vars

def concat_smash(var_addr):
        
    '''Combines a list's index values 
    and concatonates them into a string with : seperating'''
    rejoined_global_address = ":".join(var_addr)
    if rejoined_global_address[-1] != ':':
        rejoined_global_address +=":" # if there is no colon add one to the end
    print(rejoined_global_address) # Test placeholder. Remove later

    return rejoined_global_address


def prefix_length(total_address_count):
  """
  Estimates the IPv6 prefix length using an inaccurate method.

  Args:
      total_address_count: The number of expected hosts on the network.

  Returns:
      A string representing the estimated prefix length (unreliable).
  """
  estimated_prefix_length = float(total_address_count)
  estimated_prefix_length = (math.sqrt(estimated_prefix_length) / 128)
  
  actual_prefix_length = math.ceil(estimated_prefix_length)
  # This would be inaccurate and doesn't account for network/broadcast addresses
  return f"/{actual_prefix_length}"

def cider_batch_addr_write(num_segments,num_hosts_per_segment ):
    # joins the global prefix with the host bits segment
     # increments the full segments
    segment_data = {}
    key = "element"
    segments_dict = {}
    for i in range((num_segments)):
        segments_dict[key] = (f"{int(i):04x}")  # Format segment ID with leading zeros
        for j in range((num_hosts_per_segment)):  
            cc = int(j) +1
            cc = str(cc)
            host = f"host{cc}"
            j = int(j)
            address = f"{global_prefix_cider}::{j+1:04x}"  # Format host address with leading zeros
            segment_data[host] = address
            segments_dict[key] = segment_data
    return segments_dict   


def notation_select(notation): # Selects output write format
    '''
    Determines the format to write the output file
    
    Args:
        Notation: this is a string that is used to select the conditional branch
        of functions to execute

    '''

    match notation:
        case 'Cisco' | 'cisco' | 'Cis' |'cis':
            '''
            Cisco path: writes output to .json file in Cisco
            Router comand format

            Args:

            '''
            global file_out_obj, ip_file_path
            file_out_obj = format_cisco()
            ip_file_path = input(r"Enter your file name (path optional)." + "\n")
            cisco_save(file_out_obj, ip_file_path) 

        case 'CIDER' | 'cider' | 'Cider' | 'Cid' | 'cid' |'CIDR' |'cidr':
            '''
            This prints out in CIDER format, using ipv6 CIDR notation
            '''
            ver_cid_variable_forager()
            address_prefix = prefix_length(total_estimate) # calculates prefix /xx variable
            format_cider()
            write_ipv6_to_json(truncated_list)      
        case 'verbose' | 'Verbose' | 'v' | 'V':
            # Cisco router command output
            format_verbose()
            print(f"Check savefile at {ip_file_path} verbose file.")           
        case _:
            raise ValueError("error, bad input. Please try again")

        
'''---------------This is where the main program starts----------------'''
def __main__():
    global c
    while c == False:
        try:
            notation = input("How verbose should the file save (options include: Cisco, CIDER, Verbose)\n")
            if isinstance(notation, str):
                notation_select(notation) #
                c = True
            else:
                raise ValueError
        except ValueError:
            print("Invalid entry. Please enter the correct format. (Value Error)\n\n")



    # Call function to test subnet function return variable against logic table
__main__()