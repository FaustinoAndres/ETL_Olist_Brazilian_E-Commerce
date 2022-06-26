from subprocess import CompletedProcess
import logging

def capture_output(completed_process: CompletedProcess):

    if len(completed_process.stdout) > 0:
        logging.info(completed_process.stdout)
    if len(completed_process.stderr) > 0:
        logging.info(completed_process.stderr)
