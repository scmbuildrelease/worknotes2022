# worknotes2022
work notes for the history


stop huge jenkins jobs"
import hudson.model.*
def queue = Hudson.instance.queue
queue.clear()

