# region Imports
from Base import RequestBase;
from typing import Literal;
from dataclasses import dataclass;
# endregion Imports

@dataclass
class GetTeamsRequest(RequestBase):
    name: str = None;
    id: str = None;
    sport: str = None;
    league: str = None;
    division: str = None;
    conference: str = None;
    detailed: str = 'false';
    include_logos: str = 'false';
    include_records: str = 'false';

    def ApiPath(cls) -> str:
        return 'v2/players/list';

    def __post_init__(cls):
        return super().__post_init__()