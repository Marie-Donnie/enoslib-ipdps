# -*- coding: utf-8 -*-

# Imports
import inspect

from enoslib.api import run_command
from enoslib.infra.enos_vagrant.configuration import Configuration
from enoslib.types import Roles

from utils import infra, LOG


# Fig Code
def contextualize(rs: Roles):
    'Fig3. Install Galera on `database`, and Sysbench on `client` hosts.'
    run_command("apt install -y mariadb-server galera",
                pattern_hosts="database",
                roles=rs)
    run_command("curl -s https://packagecloud.io/install/repositories/akopytov/sysbench/script.deb.sh | bash; apt install -y sysbench",
                pattern_hosts="client",
                roles=rs)


# Test It!

# Define the infrastructure: 2 database machines, 2
# database/client machines, 1 net
CONF = (Configuration()
        .from_settings(backend="virtualbox")
        .add_machine(flavour="tiny", number=2, roles=["database"])
        .add_machine(flavour="tiny", number=2, roles=["database", "client"])
        .finalize())

# Setup the infra and call the `contextualize` function
with infra(CONF) as (_, roles, _):
    LOG.info(inspect.getsource(contextualize))
    contextualize(roles)
