from pathlib import Path
RunningPath=Path.cwd()
BaseDir=RunningPath.parent

class Config:
    DATABASE_PATH = BaseDir/'Data'/'Database'
    BASE_ATTRIBUTE_DB='base.db'

