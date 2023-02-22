
"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws

#create security group

web_sg = aws.ec2.SecurityGroup("web-sg",
    description="web security group",
  ingress=[
  aws.ec2.SecurityGroupIngressArgs(
  protocol="tcp",
  from_port=80,
  to_port=80,
  cidr_blocks=["0.0.0.0/0"],
       ),
  ],
)


# Create the instances
instances = []
for i in range(3):
    instance_name = f"bhuvneshpulumi-{i}"
    instance = aws.ec2.Instance(instance_name,
        ami="ami-0dfcb1ef8550277af",
        instance_type="t2.micro",
    )
pulumi.export("web_security_group_id",web_sg.id)
