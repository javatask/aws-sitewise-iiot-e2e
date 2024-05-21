# diagram.py
from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.generic.network import *
from diagrams.aws.iot import *
from diagrams.aws.general import *


with Diagram("AWS SiteWise", show=False) as diag:
    with Cluster("On-prem") as on_prem:
        with Cluster("OT Network"):
            ot_net = Switch("HiOS 1") >> Subnet("OT Network 1") >> Firewall("Firewall 1")

        edge_compute = IotGreengrass("Edge compute")
        on_prem = ot_net >> Subnet("IT Network") >> edge_compute
        

    with Cluster("AWS Cloud"):
        off_prem = on_prem >> IotSitewise("SiteWise") >> IotAnalytics("Dashboard")
        edge_compute << IotDeviceManagement("Management")

    off_prem << Users("Net Admins")
