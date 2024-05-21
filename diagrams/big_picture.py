# diagram.py
from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.generic.network import *
from diagrams.aws.iot import *
from diagrams.aws.general import *

graph_attr = {
    "dpi": "200",
    "size": "500, 300",
    "fontsize": "40",
    "labelfontsize":"30",
    "margin":"0",
    "pad": "0"
}

cluster_graph_attr = {
    "fontsize": "30",
    "labelfontsize":"30"
}

label_font_size="20"

with Diagram("AWS SiteWise", show=False, graph_attr=graph_attr) as diag:
    with Cluster("On-prem", graph_attr=cluster_graph_attr) as on_prem:
        with Cluster("OT Network", graph_attr=cluster_graph_attr):
            ot_net = Switch("HiOS 1", fontsize=label_font_size) \
                >> Subnet("OT Network 1", fontsize=label_font_size) \
                >> Firewall("Firewall 1", fontsize=label_font_size)

        edge_compute = IotGreengrass("Edge compute", fontsize=label_font_size)
        on_prem = ot_net \
            >> Subnet("IT Network", fontsize=label_font_size) \
            >> edge_compute
        

    with Cluster("AWS Cloud", graph_attr=cluster_graph_attr):
        off_prem = on_prem \
            >> IotSitewise("SiteWise", labelfloat="true", fontsize=label_font_size) \
            >> IotAnalytics("Dashboard", fontsize=label_font_size)
        edge_compute << IotDeviceManagement("Management", fontsize=label_font_size)

    off_prem << Users("Net Admins", fontsize=label_font_size)
