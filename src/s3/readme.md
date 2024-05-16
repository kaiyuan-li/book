# S3 + Remote File System

## S3

To keep S3 in sync with local fs, use the AWS CLI. For example, we have a s3 directory `s3://s3-yoshi/kongming_snapshot`. Then run this command to sync.
```
aws s3 sync s3://s3-yoshi/kongming_snapshot ~/kongming_snapshot
```

Before this, acquire the key and secret by clicking user name on the top right corner in AWS console, and select credentials. Then add them as env var in `.zshrc`.
```
export AWS_ACCESS_KEY_ID=<ID> && export AWS_SECRET_ACCESS_KEY=<KEY>
```

## Remote desktop

1. In mac, the mounted external drive is in `/Volumes` directory. Then go to settings, general, and choose to share the external drive.
1. In the client machine, right click on finders, select "connect to server" and pick the shared directory. This directory will show up under `/Volumes/` then.
