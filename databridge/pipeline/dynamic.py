import datajoint as dj
from .virtual import experiment, stimulus, fuse

schema = dj.schema("pipeline_bridge_dynamic")


# -------------------------- Data Specification --------------------------


@schema
class VideoSpec(dj.Lookup):
    definition = """
    video_id                : varchar(128)      # video specification
    ---
    fps                     : decimal(9, 6)     # frames per second
    height                  : int unsigned      # frame height (pixels)
    width                   : int unsigned      # frame width (pixels)
    channels                : int unsigned      # number of channels
    video_note = NULL       : varchar(1024)     # note about video specification
    """


@schema
class PerspectiveSpec(dj.Lookup):
    definition = """
    perspective_id          : varchar(128)      # perspective specification
    ---
    fps                     : decimal(9, 6)     # frames per second
    features                : int unsigned      # number of features
    perspective_note = NULL : varchar(1024)     # note about perspective specification
    """


@schema
class ModulationSpec(dj.Lookup):
    definition = """
    modulation_id           : varchar(128)      # modulation specification
    ---
    fps                     : decimal(9, 6)     # frames per second
    features                : int unsigned      # number of features
    modulation_note = NULL  : varchar(1024)     # note about modulation specification
    """


@schema
class ResponseSpec(dj.Lookup):
    definition = """
    response_id             : varchar(128)      # response specification
    ---
    fps                     : decimal(9, 6)     # frames per second
    response_note = NULL    : varchar(1024)     # note about response specification
    """


@schema
class TierSpec(dj.Lookup):
    definition = """
    tier_id                 : varchar(128)      # tier specification
    ---
    tier_note = NULL        : varchar(1024)     # note about tier specification
    """


# -------------------------- Processed Data --------------------------


@schema
class Video(dj.Manual):
    definition = """
    -> stimulus.Condition
    -> VideoSpec
    ---
    video                   : longblob          # [frames, height, width, channels]
    """


@schema
class Perspective(dj.Manual):
    definition = """
    -> stimulus.Trial
    -> PerspectiveSpec
    ---
    perspective             : longblob          # [frames, features]
    """


@schema
class Modulation(dj.Manual):
    definition = """
    -> stimulus.Trial
    -> ModulationSpec
    ---
    modulation              : longblob          # [frames, features]
    """


@schema
class Response(dj.Manual):
    definition = """
    -> stimulus.Trial
    -> ResponseSpec
    ---
    response                : longblob          # [frames, units]
    """


# -------------------------- Meta Data --------------------------


@schema
class TrialTier(dj.Manual):
    definition = """
    -> stimulus.Trial
    -> TierSpec
    ---
    tier                    : varchar(128)      # data tier
    """


@schema
class UnitResponse(dj.Manual):
    definition = """
    -> fuse.ScanSet.Unit
    -> ResponseSpec
    ---
    response_index          : int unsigned      # response index
    """


# -------------------------- Data Bridge --------------------------


@schema
class ScanBridge(dj.Manual):
    definition = """
    -> experiment.Scan
    -> VideoSpec
    -> PerspectiveSpec
    -> ModulationSpec
    -> ResponseSpec
    -> TierSpec
    """
