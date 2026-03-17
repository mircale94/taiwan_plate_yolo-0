# download_dataset.py
from roboflow import Roboflow

rf = Roboflow(api_key="lW69Vhz4nQARn5KWWP9t")
project = rf.workspace("xu-1mmuh").project("taiwan-license-plate-recognition-research-tlprr-dbjwq")
version = project.version(1)
dataset = version.download("yolov8")
