import json
import os, sys
# Save key names to key values in dictionary
segments = {}

def save_ipv6(segments):


    # Opens file to write
    with open( file=ip_file_path,
        mode='w') as name_save_file:
        json.dump(segments, json_file, indent=4)

def notate_translation(notation):
    match notation:
        case 'Cisco' | 'cisco' | 'Cis' |'cis':
            # Verbose output
            save_file_cisco()
        


        case 'CIDER' | 'cider' | 'Cider' | 'Cid' | 'cid':
            # CIDER output
            save_file_cider()
            
        

        case 'verbose' | 'Verbose' | 'v' | 'V':
            # Cisco router command output
                    # this loop saves addresses to the segments dictionary
            for i in range(v6Count):
        
                key = f"subnet_{i}".format(i+1)
                value = f"value_{i}".format(i+1)
                segments[key] = value

            
            save_file_verbose()
            print(f"Check savefile at {ip_file_path} verbose file.")    
            

        case _:
            raise ValueError("error, bad input. Please try again")



    

# with follows similar to a for loop. Ends in a colon


def save_file_verbose (export):
    # Defines verbose conversion function
    save_ipv6()

    return verbose_save


def save_file_cisco (export):
    # Defines Cisco conversion function. This runs a for loop to save ipv6 host addresses in a cisco router format

    return cisco_save


def save_file_cider (export):
    # Defines CIDER conversion function
    
    return cider_save

'''---------------This is where the main program starts----------------'''

# Asks for string to be used in major portions of algorithm
global_prefix = input("Please enter your Global Routing IP address (include colons).\n")

# Asks for variables that determine range and loop iterations
v6_Seg_Count = input("How many subnet segments do you want?\n")
host_estimate = input("How many hosts do you expect to use your network (total)?\n")

# Asks for output information
ip_file_path = input("Please enter the absolute path to output your file.\n")
name_save_file = input("Please name your save file output\n")

# Determines notation and format of output
notation = input("How verbose should the file save (options include: Cisco, CIDER, verbose)\n")

print(f"Global Prefix: {global_prefix}.\n" ) # Remove later
print(f"Number of Segments: {v6_Seg_Count}.\n" ) # Remove later
print(f"Total network hosts: {host_estimate}.\n" ) # Remove later
print(f"Path: {ip_file_path}.\n" ) # Remove later
print(f"File name: {name_save_file}.\n" ) # Remove later

# Calls save function to write and save file to a directory
save_ipv6(notation)









    



# Call function to test subnet function return variable against logic table



# Output into a file that saves to a directory



# with follows similar to a for loop. Ends in a colon