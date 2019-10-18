# -*- coding: utf-8 -*-

# Imports/Type defs
from typing import List

from enoslib.host import Host
from enoslib.api import run_command


# Code snippet
def contextualize(hosts: List[Host]):
    run_command("apt install -y mariadb galera", hosts)


# Extra code to execute the `contextualize` function on 3 VMs from
# Vagrant VirtualBox
from enoslib.infra.enos_vagrant.provider import Enos_vagrant
from enoslib.infra.enos_vagrant.configuration import Configuration

conf = (Configuration()
        .add_machine(flavour="tiny", number=3, roles=["database"])
        .add_network(cidr="192.168.42.0/24", roles=["database"])
        .finalize())

provider = Enos_vagrant(conf)
roles, _ = provider.init()
hosts = set(roles.values())

contextualize(hosts)
