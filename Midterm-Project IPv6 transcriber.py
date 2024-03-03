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
subnet_address = (f"{v6_Seg_Count:04x}:")

host_estimate = int(input("How many hosts do you expect to use your network (total)?\n"))
total_estimate = host_estimate + v6_Seg_Count

# Case variable to track how to calculate the print out formula
manual_or_auto = input("Manually assign host count per segment or distrbute hosts evenly?(manual, auto)\n")

if manual_or_auto == 'auto' or 'Auto' or 'a' or 'A' or 'aut' or 'Aut' or 'Au' or 'au' : # if auto option selected divides hosts by segments
    host_estimate = int(host_estimate / v6_Seg_Count)


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
              mode='w') as file_out_obj:  # file_out_obj is a placeholder variable
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
    truncated_list = network_cider_trunc(seg0, seg1, seg2)  # trunkates variables from leading zeros

    global_segment_compressed = concat_smash(truncated_list) # gobal_segment_compressed gets pulled into dictionary_fill_cider
    segments_dict, segments_data = dictionary_fill_cider(v6_Seg_Count, host_estimate, global_segment_compressed)



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


def network_cider_trunc(seg0, seg1, seg2):
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


def host_cider_trunc(seg0):
    '''Look at the global address and the host segment
    and trunkate any segment that starts ends with a zero
    and has more than one zero in succession
    '''

    hextet_vars = [seg0]  # Puts arguments into a list

    for i in range(len(hextet_vars)):
        # Check for at least two characters and two leading zeros
        if hextet_vars[i].startswith('0'):
            while len(hextet_vars[i]) > 1 and hextet_vars[i].startswith('0'):
                # Remove a single leading zero, stop if only one character remains
                hextet_vars[i] = hextet_vars[i][1:]
    hextet_vars = ''.join(map(str, hextet_vars)) # converts back into a string
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
    for i in range(0, v6_Seg_Count):
        # writes out ipv6 interface access and ip assignment commands
        print(f"interface FastEthernet0/{range(i)}\n")
        print("ipv6 enable\n")
        print(f"ipv6 address {network_address}{subnet_address[i]}{address_prefix}")


def cisco_save(save_data):
    '''need to write this to be the final function that saves dictionary in cisco format
        to a dict and finishes by running write_ipv6_to_json() function.
        TODO: Runs write_ipv6_to_json() and writes terminal print out as a pretty output
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


def dictionary_fill_cider(num_segments, num_hosts_per_segment, global_segment_compressed, segments_dict=None):
    # joins the global prefix with the subnet and host bits segments
    # increments the full segments
    match manual_or_auto:
        case 'auto' | 'Auto' | 'a' | 'A' | 'aut' | 'Aut' | 'Au' | 'au' :
            segments_dict = {}  # Create the outer dictionary

            for i in range(0, num_segments):
                network_chunk = f"{global_segment_compressed}{subnet_address}{i:04x}"  # Generate segment prefix
                segment_data = {}  # Create a new dictionary for each segment
                segment_name = f"Segment{i}"

                for j in range(0, num_hosts_per_segment):
                    host_id = j + 1  # Use descriptive variable for clarity
                    host_name = f"host{host_id}"
                    address = f"{host_id:04x}"
                    address = host_cider_trunc(address) # removes leading zeros from host address
                    address = f"{global_segment_compressed}:{address}{address_prefix}"
                    segment_data[host_name] = address


                segments_dict[segment_name] = segment_data  # Nest segment_data within segments_dict
                segments_dict[network_chunk] = segment_data  # Include a reference by prefix
        case 'man' | 'Man' | 'M' | 'm' | 'manual' | 'Manual':
            for i in range(0, num_segments): #TODO need to pull full ip addre   sses into these loops
                segment_name = input(f"Enter subnet name\n")
                network_chunk = f"{global_segment_compressed}{subnet_address}{i:04x}"  # Generate segment prefix
                segment_data = {}  # Create a new dictionary for each segment


                for j in range(0, num_hosts_per_segment):
                    host_id = j + 1  # Use descriptive variable for clarity
                    host_name = f"host{host_id}"
                    address = f"{global_segment_compressed}:{host_id:04x}"
                    address = host_cider_trunc(address) # removes leading zeros from host address
                    segment_data[host_name] = address
                segments_dict[segment_name] = segment_data  # Nest segment_data within segments_dict
                segments_dict[network_chunk] = segment_data  # Include a reference by prefix
        case _:
            raise ValueError("error, bad input. Please try again")
    return segments_dict, segment_data

def cider_batch_addr_write(segments_dict, segment_data):
    # This function prints out everything for the cider_notation
    for segmentname, netip in segments_dict.items():
        print(segmentname, )
        for hostname, ip in segment_data.items():
            print(hostname, ip)


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
print(segments_dict)
# Call function to test subnet function return variable against logic table
