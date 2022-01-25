# worknotes2022
work notes for the history


- stop huge jenkins jobs"

import hudson.model.*

def queue = Hudson.instance.queue

queue.clear()

- a useful docker reg 


docker run --name registry-browser -it -p 8082:8080 -e DOCKER_REGISTRY_URL=http://registry.xxxxx.xxxx.net klausmeyer/docker-registry-browser
