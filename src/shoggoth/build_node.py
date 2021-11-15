#!/usr/bin/env python3

# Standard Python Libraries


# Third-Party Libraries
from pyVim.connect import SmartConnect
import pyVmomi

def connection():
def get_vCenter_user():
    """Get the username for vCenter."""
    while True:
        username = input("Enter vCenter username: ")
        if re.match(EMAIL_REGEX, username):
            break
        else:
            print("Incorrectly formated email. Please try again.")

    return username


def get_password():
    """Get the password for vCenter."""
    return stdiomask.getpass()


def get_vCenter_ip() -> str:
    """Get vCenter IP address."""
    while True:
        user_input = input("Enter vCenter IPv4 address: ")
        try:
            vCenter_ip: str = ip_address(user_input)
            break
        except ValueError as err:
            # Raise error because 1 or more items were invald.
            print(err, file=sys.stderr)

    return str(vCenter_ip)


def get_os_password():

def get_vmHost():

def check_default_NIC():

def get_datastore():

def get_operator_network():

def get_number_operator():

def build_networks():

def set_autostart():

def clone_vm():

def deploy_servers():

def deploy_kalis():

def deploy_commando():

def main():
    """Shoggoth Main"""


if __name__ == "__main__":
    main()
