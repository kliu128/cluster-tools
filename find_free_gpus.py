import subprocess
from pathlib import Path
from joblib import Parallel, delayed

gpu_script = Path("./gpus.py")

cmdline = f"cd {gpu_script.parent.absolute()}; pipenv run python3 {gpu_script.absolute()}"
print(cmdline)

def check_host(host: str):
    print("Checking", host)
    proc = subprocess.run(["ssh", host, cmdline], capture_output=True)

    print(host, ":", proc.stdout, proc.stderr)

hosts = ["hyperion", "hyperion3", "turing1", "turing2", "turing3", "turing4", "hyperturing1", "hyperturing2"]

Parallel(n_jobs=8, backend="threading")(
             map(delayed(check_host), hosts))