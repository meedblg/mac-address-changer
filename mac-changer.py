import subprocess
import optparse
import re


# take the options from user 
def parse_args():
    parser = optparse.OptionParser()
    parser.add_option('--i','--nic',dest="network_interface", help="This Place For Network Interface ")
    parser.add_option('--m', '--mac',dest="mac_address", help="This Place For New MAC Address")
    options, argument = parser.parse_args()
    
    if not options.network_interface:
        print("[-] You Forget To Type Network Interface... ")
        exit()
    if not options.mac_address:
        print("[-] You Forget TO type MAC Address...")
        exit()
    return options

# run the commands for changing mac address
def mac_changer(network_interface, mac_address):
    subprocess.call("ifconfig " + options.network_interface + " down", shell=True)
    subprocess.call("ifconfig " + options.network_interface + " hw ether " + options.mac_address, shell=True)
    subprocess.call("ifconfig " + options.network_interface + " up", shell=True)
    print("[*]  Changing Mac Address For " + options.network_interface + " To " + options.mac_address)
    subprocess.call("sleep 2 ", shell=True)

# regex the mac address from ifconfig to compare with new mac adrees 
def get_mac(network_interface):
    mac = subprocess.check_output("ifconfig").decode("UTF-8")
    mac_resault = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", mac)
    return mac_resault[0]

options = parse_args()
mac_changer(options.network_interface, options.mac_address) 
mac_resault = get_mac(options.network_interface)

if mac_resault == options.mac_address:
    print ("[*] MAC Address Changed Successfully To " + options.mac_address )
else:
    print("[-] Somthing Went Wrong...!! ")
    subprocess.call("sleep 2 ", shell=True)
    print("[-] Type a Valid MAC address... and Run With Sudo")

