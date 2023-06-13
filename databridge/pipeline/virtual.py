from datajoint import create_virtual_module

experiment = create_virtual_module("experiment", "pipeline_experiment")
stimulus = create_virtual_module("stimulus", "pipeline_stimulus")
fuse = create_virtual_module("fuse", "pipeline_fuse")