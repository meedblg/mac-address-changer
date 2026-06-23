## MAC Changer

## A simple Python tool to change the MAC address of a network interface on Linux systems.

## Features
Change the MAC address of any network interface.
Verify that the MAC address was changed successfully.
Simple command-line usage.
Requirements
Python 3
Linux
ifconfig installed
Root privileges (sudo)
## Installation
git clone https://github.com/yourusername/mac-changer.git
## Usage
sudo python3 mac-changer.py --i eth0 --m 00:11:22:33:44:55

--i	Network interface (e.g. eth0, wlan0)

--m	New MAC address

## Example
sudo python3 mac-changer.py --i wlan0 --m 00:11:22:33:44:55
## Output

 [*] Changing Mac Address For wlan0 To 00:11:22:33:44:55
 [*] MAC Address Changed Successfully To 00:11:22:33:44:55

## Author

Meed BLG

