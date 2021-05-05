import os
import shutil

os.unlink('filter_plugins/.keep')
os.unlink('inventory/group_vars/.keep')
shutil.rmtree('licenses')
