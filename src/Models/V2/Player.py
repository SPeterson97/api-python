#region Imports
from Base import ModelBase;
from dataclasses import dataclass
#endregion Imports

@dataclass
class Player(ModelBase):
    id: str = None;
    player_name: str = None;
    sport: str = None;
    league: str = None;
    first_name: str = None;
    last_name: str = None;
    team_name: str = None;
    team_id: str = None;
    number: str = None;
    position: str = None;
    age: str = None;
    height: str = None;
    weight: str = None;