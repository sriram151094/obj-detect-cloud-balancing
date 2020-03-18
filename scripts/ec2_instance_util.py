# ami-0903fd482d7208724
import urllib3
from connection_util import get_ec2_resource


def generate_ec2_pair():
    ec2 = get_ec2_resource()
    outfile = open('cloud_project1.pem', 'w')
    key_pair = ec2.create_key_pair(KeyName='cloud_project1')
    KeyPairOut = str(key_pair.key_material)
    outfile.write(KeyPairOut)


def create_ec2_instances(num_of_instances, ec2_resource):
    if num_of_instances > 0:
        # ec2 = get_ec2_resource()
        instances = ec2_resource.create_instances(
            ImageId='ami-001aaa7b482ada63a',
            Monitoring={
                'Enabled': True
            },
            MaxCount=num_of_instances,
            SecurityGroupIds=[
                'sg-0094672f5c9a5f124'
            ],
            IamInstanceProfile={
                'Arn': 'arn:aws:iam::051954823249:instance-profile/ec2cloudinstance'
            },
            MinCount=1,
            KeyName="cloud_project1",
            InstanceType="t2.micro"
        )
        for instance in instances:
            instance.wait_until_running()
        return instance


def get_all_ec2_instances(ec2_resource):
    # ec2 = get_ec2_resource()
    return ec2_resource.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running', 'stopped']}])


def get_running_ec2_instances(ec2_resource):
    # ec2 = get_ec2_resource()
    return ec2_resource.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])


def get_idle_instances(ec2_resource):
    return ec2_resource.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])


def start_instances(instances, ec2_client):
    InstanceIDs = []
    for instance in instances:
        InstanceIDs.append(instance.id)
        print(instance.id, instance.instance_type)

    ec2_client.start_instances(
        InstanceIds=InstanceIDs)


# def stop_instance(ec2_client):
#     instance_id = urllib3.request.urlopen('http://169.254.169.254/latest/meta-data/instance-id').read().decode()
#     response = ec2_client.stop_instances(
#         InstanceIds=[
#             instance_id,
#         ]
#     )


if __name__ == '__main__':
    # generate_ec2_pair()
    # x = get_running_ec2_instances(get_ec2_resource())
    # y = sum(1 for _ in x)
    # print(y)
    create_ec2_instances(1, get_ec2_resource())
