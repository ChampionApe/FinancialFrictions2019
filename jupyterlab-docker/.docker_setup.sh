#!/bin/bash

# Set an option to exit immediately if any error appears
set -o errexit

echo '{
  "experimental": true,
  "storage-driver": "overlay2",
  "max-concurrent-downloads": 50,
  "max-concurrent-uploads": 50
}' | sudo tee /etc/docker/daemon.json
sudo service docker restart
