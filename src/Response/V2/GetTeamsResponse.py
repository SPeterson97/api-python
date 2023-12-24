#region Imports
import json;
from Models.V2 import Team;
from Base import ResponseBase;
#endregion Imports

class GetTeamsResponse(ResponseBase):
    def __init__(self, response: str):
        super().__init__(response);
        resp = json.loads(response);
        obj = self.ParseResponse(json.dumps(resp['data']));
        self.Teams = [Team(**t) for t in obj]

    def ParseResponse(self, response: str):
        try:
            return json.loads(response);
        except Exception as ex:
            return ex;