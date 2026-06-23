import subprocess
import optparse
import re


# take the options from user 
parser = optparse.OptionParser()
parser.add_option('--i','--nic',dest="network_interface", help="This Place For Network Interface ")
parser.add_option('--m', '--mac',dest="mac_address", help="This Place For New MAC Address")
options, argument = parser.parse_args()
 
# run the commands for changing mac address
subprocess.call("ifconfig " + options.network_interface + " down", shell=True)
subprocess.call("ifconfig " + options.network_interface + " hw ether " + options.mac_address, shell=True)
subprocess.call("ifconfig " + options.network_interface + " up", shell=True)
print("[*] - Changing Mac Address For " + options.network_interface + " To " + options.mac_address)
subprocess.call("sleep 2 ", shell=True)

# regex the mac address from ifconfig to compare with new mac adrees 
mac = subprocess.check_output("ifconfig").decode("UTF-8")
mac_resualt = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", mac)

if mac_resualt[0] == options.mac_address:
    print ("[*] MAC Address Changed Successfully To " + options.mac_address )
else:
    print("[-] Somthing Went Wrong...!! ")
    subprocess.call("sleep 2 ", shell=True)
    print("[-] Type a Valid MAC address... and Run With Sudo")

