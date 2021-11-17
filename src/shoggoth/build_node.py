#!/usr/bin/env python3

# Standard Python Libraries
from ipaddress import ip_address
import re
import sys

# Third-Party Libraries
from pyVim.connect import SmartConnect
from pyVmomi import vim
import stdiomask

EMAIL_REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


def connect():
    vCenter_ip = get_ip("Enter vCenter IPv4 address")
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
            vCenter_ip = get_ip("Enter vCenter IPv4 address")

        except vim.fault.InvalidLogin as err:
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


def get_ip(msg) -> str:
    """Get vCenter IP address."""
    while True:
        user_input = input(f"{msg}: ")
        try:
            ip: str = ip_address(user_input)
            break
        except ValueError as err:
            # Raise error because 1 or more items were invald.
            print(err, file=sys.stderr)

    return str(ip)


def get_os_password():
    pass


def get_vmHost(content):
    """Get vmHost from vCenter."""

    # Get a list of nodes from vCenter
    host_view = content.viewManager.CreateContainerView(
        content.rootFolder, [vim.HostSystem], True
    )
    nodes = [host for host in host_view.view]

    # Holds the node names for input validation/location.
    node_names = list()

    # Display the node names in a list.
    print("Nodes: ")
    for node in nodes:
        if node.runtime.connectionState == "connected":
            node_names.append(node.name)
            print(f"\t{node.name}")

    print()
    # Ask for node name and compare to list of possible names
    while True:
        vmHost_ip = get_ip("Enter node IP from above")
        if vmHost_ip in node_names:
            # Gets the vmHost from the list of nodes.
            vmHost = nodes[node_names.index(vmHost_ip)]
            break
        else:
            print("Incorrect Node, please check your input.")

    host_view.Destroy()
    return vmHost


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
