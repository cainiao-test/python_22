import os


class ProjectPath:
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(ROOT_PATH, 'data')
    CONFIG_PATH = os.path.join(ROOT_PATH, 'setting')


p_path = ProjectPath()
