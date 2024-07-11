import os
import subprocess

def download_models_setup():
    dot_config_path = os.path.join(os.environ.get('HOME'), '.config')
    instruct_config_path = os.path.join(dot_config_path, 'instructlab')
    instruct_models_path = os.path.join(dot_config_path, 'models')

    if os.path.isfile(instruct_models_path):
        pass
    else:
        os.makedirs(instruct_models_path, exist_ok=True)
        os.chdir(instruct_config_path)
        p = subprocess.Popen(f"ilab model download", shell=True)
        p.wait()
