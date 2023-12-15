#region Imports
import json;
from Models.V2 import Player;
from Base import ResponseBase;
#endregion Imports

class GetPlayersResponse(ResponseBase):
    def __init__(self, response: str):
        super().__init__(response);
        resp = json.loads(response);
        obj = self.ParseResponse(json.dumps(resp['data']));
        self.Players = [p for p in obj]

    def ParseResponse(self, response: str):
        try:
            return json.loads(response, object_hook=lambda d: Player(**d));
        except Exception as ex:
            return ex;