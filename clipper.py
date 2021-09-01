from dotenv import load_dotenv
import ecs_client as ecs

load_dotenv()

def print_line():
    print("-----------------------------")

cluster_name = ecs.get_cluster()
print_line()
service_description = ecs.get_service_description(cluster_name)
print_line()
# print("Service ARN: " + service_description['services'][0]['serviceArn'])
print("Service Name: " + service_description['services'][0]['serviceName'])
print("Desired Count: " + str(service_description['services'][0]['desiredCount']))
print("Running Count: " + str(service_description['services'][0]['runningCount']))

print_line()
ecs.update_service(cluster_name, service_description)
