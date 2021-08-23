import py3nvml
import os

py3nvml.grab_gpus(num_gpus=10, gpu_fraction=0.7, max_procs=10)
print(os.getenv("CUDA_VISIBLE_DEVICES"))