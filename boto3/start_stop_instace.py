import boto3
# Resource <--- Client (Low Level)
ec2 = boto3.resource('ec2')

#print(ec2,)
#print(*dir(ec2), sep='\n')

for instance in ec2.instances.all():
    if instance.state["Name"] == 'stopped':
        instance.start()
        print("Stating Instance", instance.id)
    else:
        print("Alread Started: ", instance.id, "State: ", instance.state)
        if instance.id == "i-070a496d99c9b3043" and instance.state['Name'] == 'running':
            print("Stopping Desired Instance")
            instance.stop()
    #instance.start()
