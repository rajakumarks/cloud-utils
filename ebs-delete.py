import boto3
import logging
#setup simple logging for INFO
logger = logging.getLogger()
logger.setLevel(logging.INFO)
#define the connection
ec2 = boto3.resource('ec2',region_name='us-east-1')

def deleteVol(tobeDeleted):
    if len(tobeDeleted) == 0:
        print ("No volumes to terminate! Exiting.")
        exit()
    for i in tobeDeleted:
        print('Deleting volume {0}'.format(i.id))
        i.delete()
def lambda_handler(event, context):
    print("event " + str(event))
    print("context " + str(context))
    #use the filter() of the instancess collection to retrieve
    filters = [
        {
            'Name': 'tag:PLATFORM',
            'Values': ['RAJ-TEST']

        }
    ]
    #filter the volumes
    volumes = ec2.volumes.filter(Filters=filters)
    #locate all available volumes
    to_delete = []
    for vol in volumes:
        if (vol.state == 'available'):
            to_delete.append(vol)
    #print(to_delete.id)
    if(len(to_delete) != 0:
      deleteVol(to_delete)
    else:
      print("No volumes are available to delete)
