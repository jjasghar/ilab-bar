import os
import subprocess

# check for configuration file at ~/.config/instructlab/config.yaml
# if file is not there create a sane default
def configuration_setup():
    dot_config_path = os.path.join(os.environ.get('HOME'), '.config')
    instruct_config_path = os.path.join(dot_config_path, 'instructlab')
    instruct_config = os.path.join(instruct_config_path, 'config.yaml')

    if os.path.isfile(instruct_config):
        pass
    else:
        if os.path.isfile(instruct_config_path) == None:
            os.makedirs(instruct_config_path)
        os.chdir(instruct_config_path)
        p = subprocess.Popen(f"/usr/local/bin/instructlab init --non-interactive", shell=True)
        p.wait()
