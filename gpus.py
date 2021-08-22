import py3nvml

free_gpus = py3nvml.get_free_gpus()
print(free_gpus)