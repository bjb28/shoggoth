#!/usr/bin/env python3

"""Drops into an iPython session after connecting to vCenter
and getting a vmHost."""

# Third-Party Libraries
from IPython import embed

# Customer Libraries
from shoggoth.build_node import connect, get_vmHost


def main():
    """Dev-Console Main"""

    vCenter = connect()
    content = vCenter.RetrieveContent()
    vmHost = get_vmHost(content)

    embed()


if __name__ == "__main__":
    main()