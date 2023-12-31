from typing import Dict, List

from ..common import BaseStruct

from msgspec import field


class ItemBundle(BaseStruct):
    id_: str = field(name='id')
    count: int
    type_: str = field(name='type')


class SpCharMissionData(BaseStruct):
    charId: str
    missionId: str
    sortId: int
    condType: str
    param: List[str]
    rewards: List[ItemBundle]


class CharMetaTable(BaseStruct):
    __version__ = '23-12-02-09-28-50-918524'

    spCharGroups: Dict[str, List[str]]
    spCharMissions: Dict[str, Dict[str, SpCharMissionData]]
    spCharVoucherSkinTime: Dict[str, int]
