from diagrams import Diagram, Cluster, Edge
from diagrams.aws.network import APIGateway, ELB, CloudFront
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS, Dynamodb
from diagrams.aws.storage import S3
from diagrams.aws.management import Cloudwatch
from diagrams.aws.security import IAM

with Diagram("NASA Mars Rover Photos API Architecture", show=False):
    user = APIGateway("Amazon API Gateway")

    with Cluster("Application Layer"):
        lb = ELB("AWS ELB\nLoad Balancer")
        with Cluster("Server Cluster"):
            app_server1 = EC2("App Server 1 (EC2)")
            app_server2 = EC2("App Server 2 (EC2)")
            app_server3 = EC2("App Server 3 (EC2)")

    with Cluster("Database Layer"):
        db_primary = RDS("Amazon RDS Primary DB")
        with Cluster("Read Replicas"):
            db_read_replica1 = RDS("Read Replica 1")
            db_read_replica2 = RDS("Read Replica 2")

    cache = Dynamodb("Amazon DynamoDB Cache")
    storage = S3("Amazon S3 Image Storage")
    cdn = CloudFront("Amazon CloudFront CDN")
    monitoring = Cloudwatch("Amazon CloudWatch")
    security = IAM("AWS IAM")

    user >> Edge(label="API Calls") >> lb >> [app_server1, app_server2, app_server3]
    app_server1 >> Edge(label="Read/Write") >> db_primary
    app_server2 >> Edge(label="Read/Write") >> db_primary
    app_server3 >> Edge(label="Read/Write") >> db_primary

    app_server1 >> Edge(label="Read") >> db_read_replica1
    app_server2 >> Edge(label="Read") >> db_read_replica2
    app_server3 >> Edge(label="Read") >> db_read_replica1

    app_server1 >> Edge(label="Query") >> cache
    app_server2 >> Edge(label="Query") >> cache
    app_server3 >> Edge(label="Query") >> cache

    app_server1 >> Edge(label="Store/Fetch") >> storage
    app_server2 >> Edge(label="Store/Fetch") >> storage
    app_server3 >> Edge(label="Store/Fetch") >> storage

    storage >> Edge(label="Distribute") >> cdn

    app_server1 >> Edge(label="Monitor") >> monitoring
    app_server2 >> Edge(label="Monitor") >> monitoring
    app_server3 >> Edge(label="Monitor") >> monitoring

    user >> Edge(label="Authenticate") >> security
