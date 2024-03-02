import json
import os, sys
# Save key names to key values in dictionary

    # Asks for string to be used in major portions of algorithm
# global_prefix = input("Please enter your Global Routing IP address (include colons).\n")
global_prefix = "2001:0451:0051:0001" # Placeholder
global_prefix_cider = ''
host_segment = '0000:0000:0000:0000'
# Determines notation and format of output
notation = input("How verbose should the file save (options include: Cisco, CIDER, verbose)\n")
                    
# Asks for variables that determine range and loop iterations
v6_Seg_Count = input("How many subnet segments do you want?\n")
host_estimate = input("How many hosts do you expect to use your network (total)?\n")

# Case variable to track how to calculate the print out formula
host_distribute = input("Manually assign host count per segment or distrbute hosts evenly?\n")

# Asks for output information
ip_file_path = input(r"Enter your file name (path optional)." + "\n")

truncated_list = []
segments = {}
_ = ''

def write_ipv6_to_json(segments): # Write file function
    '''
    Writes data to a json file, adds a new line after every entry

    Args: 
        ip_file_path: The absolute or relative path the user set 
        (Global Variable needs to be defined before running this function)

        file_out_obj: the name of the .json file being written to
    '''

    with open( file=ip_file_path, # Opens file to write and Designates the writing filepath 
        mode='w') as file_out_obj: # file_out_obj is a placeholder variable
        json.dump(segments, file_out_obj, indent=4)
        file_out_obj.write('\n')  # Add a newline after each entry
        # Still need to write function component that exports all data to save file


    # Defines CIDER conversion function
    
    pass

def format_verbose (export): # Defines verbose conversion format
                        # this loop saves addresses to the segments dictionary
            for i in range(v6Count):
        
                key = f"subnet_{i}".format(i+1)
                value = f"value_{i}".format(i+1)
                segments[key] = value
            write_ipv6_to_json()
            pass


def format_cisco (export):
    # Defines Cisco conversion function. This runs a for loop to save ipv6 host addresses in a cisco router format

    return cisco_save

def format_cider():
    '''
    CIDER path: writes output to .json in cider networking
    format. *NOTE* Zero suppression includes all leading zeros
            **Please chcek to see if your network configuration tool
            **or fixture uses the same or different trunkation format
            **before plug-and-playing .json file     
    '''

    seg0, seg1, seg2, seg3 = cider_slice() # Slices the global address into hextets
    
    truncated_list = cider_trunc(seg0, seg1, seg2, seg3) # trunkates variables from leading zeros

    global_prefix_cider = concat_smash(truncated_list)



def cider_slice():
    
    '''Variable for splitting the global address into
    substring variables

        Args:
            seg0 - seg3: these strings are used to slice and hold
            the global IP address  
    '''
    seg0_0to3 = global_prefix[0:4]
    seg1_5to8= global_prefix[5:9]
    seg2_10to13 = global_prefix[10:14]
    seg3_15to18 = global_prefix[15:19]
    return seg0_0to3, seg1_5to8, seg2_10to13, seg3_15to18

def cider_trunc(seg0, seg1, seg2, seg3):
    '''Look at the global address and the host segment
    and trunkate any segment that starts ends with a zero
    and has more than one zero in succession
    '''
    
    hextet_vars = [seg0, seg1, seg2, seg3] # Puts arguments into a list

    for i in range(len(hextet_vars)):
        # Check for at least two characters and two leading zeros
        if len(hextet_vars[i]) > 1 and hextet_vars[i].startswith('0'):  
            while len(hextet_vars[i]) > 1 and hextet_vars[i].startswith('0'):

                # Remove a single leading zero, stop if only one character remains
                hextet_vars[i] = hextet_vars[i][1:]  

    return hextet_vars

def concat_smash(var_addr):
        
    '''Ccombines a list's index values 
    and concatonates them into a string with : seperating'''
    rejoined_global_address = ":".join(var_addr)
    print(rejoined_global_address)

    return rejoined_global_address

def cider_batch_addr_write(global_prefix_cider):
     for i in v6_Seg_Count:
          segments = (global_prefix_cider).join(host_segment)
     

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
                format_cisco()
                
            case 'CIDER' | 'cider' | 'Cider' | 'Cid' | 'cid':
                format_cider()
                write_ipv6_to_json(truncated_list)
                
                
            
            case 'verbose' | 'Verbose' | 'v' | 'V':
                # Cisco router command output
                format_verbose()
                print(f"Check savefile at {ip_file_path} verbose file.")    
                

            case _:
                raise ValueError("error, bad input. Please try again")



'''---------------This is where the main program starts----------------'''


notation_select(notation)


# Call function to test subnet function return variable against logic table