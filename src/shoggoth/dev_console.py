#!/usr/bin/env python3

"""Drops into an iPython session after connecting to vCenter
and getting a vmHost."""

# Third-Party Libraries
from IPython import embed

# Customer Libraries
from shoggoth.build_node import connect, get_datastore, get_vmHost


def main():
    """Dev-Console Main"""

    vCenter = connect()
    content = vCenter.RetrieveContent()
    vmHost = get_vmHost(content)
    datastore = get_datastore(vmHost.datastore)
    embed()


if __name__ == "__main__":
    main()
