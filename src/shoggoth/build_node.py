#!/usr/bin/env python3

# Standard Python Libraries
from ipaddress import ip_address
import re
import sys

# Third-Party Libraries
from pyVim.connect import SmartConnect
import pyVmomi
import stdiomask

EMAIL_REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


def connect():
    vCenter_ip = get_vCenter_ip()
    vCenter_user = get_vCenter_user()
    vCenter_password = get_password()

    while True:
        try:
            connection = SmartConnect(
                host=vCenter_ip,
                user=vCenter_user,
                pwd=vCenter_password,
                disableSslCertValidation=True,
            )
            break
        except ConnectionRefusedError as err:
            print(str(err))
            print("Error with vCenter IP. Please check.")
            vCenter_ip = get_vCenter_ip()

        except pyVmomi.vim.fault.InvalidLogin as err:
            print(err.msg)
            print("Please re-enter the username and password.")
            vCenter_user = get_vCenter_user()
            vCenter_password = get_password()

    return connection


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
    pass


def get_vmHost():
    pass


def check_default_NIC():
    pass


def get_datastore():
    pass


def get_operator_network():
    pass


def get_number_operator():
    pass


def build_networks():
    pass


def set_autostart():
    pass


def clone_vm():
    pass


def deploy_servers():
    pass


def deploy_kalis():
    pass


def deploy_commando():
    pass


def main():
    """Shoggoth Main"""
    pass


if __name__ == "__main__":
    main()
