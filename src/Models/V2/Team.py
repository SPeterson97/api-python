#region Imports
from Base import ModelBase;
from dataclasses import dataclass
#endregion Imports

@dataclass
class Team(ModelBase):
    id: str = None;
    team_name: str = None;
    team_city: str = None;
    team_mascot: str = None;
    team_abbreviation: str = None;
    sport: str = None;
    league: str = None;
    logo: str = None;
    team_nickname: str = None;
    division: str = None;
    conference: str = None;
    records: dict = None;