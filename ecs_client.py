import boto3
import os

client = boto3.client(
    "ecs",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)

def get_cluster():
    for index, clusterArn in enumerate(client.list_clusters()["clusterArns"]):
        print(f'{index}: {clusterArn}')

    selected_cluster = int(input("Select cluster: "))

    return client.list_clusters()["clusterArns"][selected_cluster].split("/")[-1]

def get_service_description(cluster):
    service_arns = client.list_services(
        cluster=cluster,
        maxResults=25
    )['serviceArns']

    for index, serviceArn in enumerate(service_arns):
        print (str(index) + ": " + serviceArn)

    selected_service = int(input("Select a service: "))

    return client.describe_services(
        cluster=cluster,
        services=[service_arns[selected_service]]
    )

def update_service(cluster, service_description):
    print("Select an action")
    print("0. Force new deployment")
    print("1. Turn off service (set desired task to 0)")
    print("2. Turn on service (set desired task to 1)")
    selected_action = input(">")

    if selected_action == str(0):
        response = client.update_service(
            cluster=cluster,
            service=service_description['services'][0]['serviceName'],
            forceNewDeployment=True
        )

        print(response)
    elif selected_action == str(1):
        response = client.update_service(
            cluster=cluster,
            service=service_description['services'][0]['serviceName'],
            desiredCount=0
        )

        print(response)
    elif selected_action == str(2):
        response = client.update_service(
            cluster=cluster,
            service=service_description['services'][0]['serviceName'],
            desiredCount=1
        )

        print(response)
    else:
        print("Invalid selection")
