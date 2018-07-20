import os

# scp -i [path to private key] [path to image] [group name]@54.144.16.81:/home/iot/[group name]
cmd = "scp -i group1 cat.jpg group1@35.173.122.2:/home/iot/Group01"
os.system(cmd)

