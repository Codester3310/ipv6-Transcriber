import json, math

# Save key names to key values in dictionary

# Asks for string to be used in major portions of algorithm
# network_address = input("Please enter your Global Routing IP address (include colons).\n")
network_address = "2001:0451:0051"  # Placeholder
global_prefix_cider = ''
host_segment = '0000:0000:0000:0000'
# Determines notation and format of output
notation = input("How verbose should the file save (options include: Cisco, CIDER, verbose)\n")

# Asks for variables that determine range and loop iterations
v6_Seg_Count = int(input("How many subnet segments do you want?\n"))

''' subnet_address is the largest subnet addr defined. 
    Increment downwards till zero to use all subnets
    OR increment from zero till your index is greater than subnet_address
'''
subnet_address = (f"{v6_Seg_Count:04x}")

host_estimate = int(input("How many hosts do you expect to use your network (total)?\n"))
total_estimate = host_estimate + v6_Seg_Count

# Case variable to track how to calculate the print out formula
host_distribute = input("Manually assign host count per segment or distrbute hosts evenly?\n")

# Asks for output information
ip_file_path = input(r"Enter your file name (path optional)." + "\n")

truncated_list = []
segments_dict = {}
_ = ''


def write_ipv6_to_json(segmentsW):  # Write file function
    '''
    Writes data to a json file, adds a new line after every entry

    Args: 
        ip_file_path: The absolute or relative path the user set 
        (Global Variable needs to be defined before running this function)

        file_out_obj: the name of the .json file being written to
    '''

    with open(file=ip_file_path,  # Opens file to write and Designates the writing filepath
              mode='w', encoding=object) as file_out_obj:  # file_out_obj is a placeholder variable
        json.dump(segmentsW, file_out_obj, indent=4)
        file_out_obj.write('\n')  # Add a newline after each entry
        # Still need to write function component that exports all data to save file

    # Defines CIDER conversion function

    pass


def format_verbose():  # Defines verbose conversion format
    # this loop saves addresses to the segments dictionary
    for i in (v6_Seg_Count):
        key = f"subnet_{i}".format(i + 1)
        value = f"value_{i}".format(i + 1)
        segments_dict[key] = value
    write_ipv6_to_json(segments_dict)
    pass


def format_cisco(export):
    # Defines Cisco conversion function. This runs a for loop to save ipv6 host addresses in a cisco router format

    return cisco_save(segments_dict)


def format_cider():
    '''
    CIDER path: writes output to .json in cider networking
    format. *NOTE* Zero suppression includes all leading zeros
            **Please chcek to see if your network configuration tool
            **or fixture uses the same or different trunkation format
            **before plug-and-playing .json file     
    '''
    address_prefix = prefix_length(total_estimate)
    seg0, seg1, seg2 = cider_slice()  # Slices the global address into hextets
    truncated_list = cider_trunc(seg0, seg1, seg2)  # trunkates variables from leading zeros

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
    seg1_5to8 = network_address[5:9]
    seg2_10to13 = network_address[10:14]

    return seg0_0to3, seg1_5to8, seg2_10to13


def cider_trunc(seg0, seg1, seg2):
    '''Look at the global address and the host segment
    and trunkate any segment that starts ends with a zero
    and has more than one zero in succession
    '''

    hextet_vars = [seg0, seg1, seg2]  # Puts arguments into a list

    for i in range(len(hextet_vars)):
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
        rejoined_global_address += ":"  # if there is no colon add one to the end
    print(rejoined_global_address)  # Test placeholder. Remove later

    return rejoined_global_address


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


def cisco_save(save_data):
    '''need to write this to be the final function that saves dictionary in cisco format
        to a dict and finishes by running write_ipv6_to_json() function.
    '''
    pass


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


def cider_batch_addr_write(num_segments, num_hosts_per_segment):
    # joins the global prefix with the host bits segment
    # increments the full segments

    for i in (num_segments):
        segments_dict = (f"{global_prefix_cider}{int(i):04x}")  # Format segment ID with leading zeros
        segment_data = {}
        for j in (num_hosts_per_segment):
            cc = int(j) + 1
            cc = str(cc)
            host = f"host{cc}"
            j = int(j)
            address = f"{global_prefix_cider}::{j + 1:04x}"  # Format host address with leading zeros
            segment_data[host] = address
        segments_dict[global_prefix_cider] = segment_data
    return segments_dict


def notation_select(notation):  # Selects output write format
    '''
    Determines the format to write the output file
    
    Args:
        Notation: this is a string that is used to select the conditional branch
        of functions to execute

    '''

    match notation:
        case 'Cisco' | 'cisco' | 'Cis' | 'cis':
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
address_prefix = prefix_length(total_estimate)  # calculates prefix /xx variable

notation_select(notation)

# Call function to test subnet function return variable against logic table
