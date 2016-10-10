# cloudsnapshots

usage: createsnap.py [-h] -v VOLUME_IDS [VOLUME_IDS ...] [-s SAFEMODE]
                     [-t SERVERNAME] [-n NAMETAG] [-r REGION] [-d DELETEFLAG]

create aws snapshots from vol-id

optional arguments:
  -h, --help            show this help message and exit
  -v VOLUME_IDS [VOLUME_IDS ...], --volume-ids VOLUME_IDS [VOLUME_IDS ...]
                        snapshot id
  -s SAFEMODE, --safemode SAFEMODE
                        set the dry run flag
  -t SERVERNAME, --servername SERVERNAME
                        Please provide the data to populate ServerName tag
  -n NAMETAG, --nametag NAMETAG
                        set the Name tag for the snapshot
  -r REGION, --region REGION
                        region where you want to manage snapshots
  -d DELETEFLAG, --deleteflag DELETEFLAG
                        set delete tag on/off
