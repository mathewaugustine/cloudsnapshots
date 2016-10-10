from boto.ec2 import connect_to_region
import boto3
from datetime import datetime, timedelta
import sys
import argparse
import time



parser = argparse.ArgumentParser(description='create aws snapshots from vol-id')
parser.add_argument('-v', '--volume-ids',
                        dest='volume_ids',
                        required=True,
                        nargs='+',
                        help='snapshot id')
parser.add_argument('-s', '--safemode',
			            required=False,
			            default='True',
                        help='set the dry run flag')

parser.add_argument('-t', '--servername',
                        required=False,
                        default=None,
                    help='Please provide the data to populate ServerName tag')
parser.add_argument('-n', '--nametag',
                        default=None,
			            required=False,
                        help='set the Name tag for the snapshot')
parser.add_argument('-r', '--region',
                        required=False,
                        type=str,
						default='ap-southeast-2',
                        help='region where you want to manage snapshots')
parser.add_argument('-d', '--deleteflag',
                        required=False,
                        type=str,
						default='on',
                        help='set delete tag on/off')

args = parser.parse_args()
#set the tag filters to prevent accidental deletion
servername = str(args.servername) # accept ServerName tag value from commandline

if (args.servername == None):
    parser.print_help()
    sys.exit()


if (args.nametag == None):
	tagnameforsnap = servername + '_' + time.strftime("%Y_%m_%d")
else:
    tagnameforsnap = args.nametag

if (args.safemode == 'True'):
    args.safemode = bool(True)
else:
    print('Safemode Disabled')
    args.safemode = bool(False)

if (args.deleteflag == 'on'):
	delflag = 'on'
else:
    delflag = ''


ec2 = connect_to_region(str(args.region))


print tagnameforsnap
filters = {
    "Name" : tagnameforsnap,
	"ServerName" : servername,
	"delflag" : delflag
}

new_snapshot_list = []

#loop through and delete until count is reaching the keep value
for volumeid in args.volume_ids:
    print('creating snapshot for {0}: servername {1}' \
                            .format(volumeid,servername) )
    try:
        new_snapshot = ec2.create_snapshot(volume_id=volumeid, \
                description='Snapshot of {1}:{0}'.format(volumeid,servername),\
                dry_run=args.safemode )
        new_snapshot_list.append(new_snapshot)
        #print new_snapshot_list
    except Exception as e:
        print "Dry MODE is set to:{0}".format(args.safemode)
        print('Use option -s False to override')
        print e

for snapshot in new_snapshot_list:
    time.sleep(6)
    print('{0} created').format(snapshot)
    #snapshot.wait_until_completed()
    print('adding filters')
    snapshot.add_tags(filters)
