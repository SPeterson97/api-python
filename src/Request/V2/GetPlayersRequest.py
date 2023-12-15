# region Imports
from Base import RequestBase;
from typing import Literal;
from dataclasses import dataclass;
# endregion Imports

@dataclass
class GetPlayersRequest(RequestBase):
    name: str = None;
    id: str = None;
    sport: str = None;
    league: str = None;
    team: str = None;
    is_active: bool = True;
    include_logos: bool = False;
    page: int = None;

    def ApiPath(cls) -> str:
        return 'v2/players/list';

    def __post_init__(cls):
        return super().__post_init__()