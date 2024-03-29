from diagrams import Cluster, Diagram, Node
from diagrams.onprem.inmemory import Redis


OUTPUT_DIRECTORY = "./output"


with Diagram(
    "Pandas Dashboard", filename=f"{OUTPUT_DIRECTORY}/architecture", show=False
):
    cache = Redis("Redis")
    producer = Node("Producer App", shape="box")
    consumer = Node("FastAPI App", shape="box")

    producer >> cache >> consumer