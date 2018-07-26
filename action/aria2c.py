import json

import requests

def success(response):

    result = response.json()
    return json.dumps(result, indent=2, ensure_ascii=False).encode('utf8')


class Aria2c:

    '''

    Example : 

    

      client = Aria2c('localhost', '6800')

 

      # print server version

      print(client.getVer())

      

      # add a task to server 

      client.addUri('http://example.com/file.iso')

      

      # provide addtional options 

      option = {"out": "new_file_name.iso"}

      client.addUri('http://example.com/file.iso', option)

    '''

    IDPREFIX = "pyaria2c"

    ADD_URI = 'aria2.addUri'

    GET_VER = 'aria2.getVersion'



    def __init__(self, host, port, token=None):

        self.host = host

        self.port = port

        self.token = token

        self.serverUrl = "http://{host}:{port}/jsonrpc".format(**locals())

    

    def _genPayload(self, method, uris=None, options=None, cid=None):

        cid = IDPREFIX + cid if cid else Aria2c.IDPREFIX

        p = {

            'jsonrpc': '2.0', 

            'id': cid,

            'method': method,

            }

        if self.token is not None: 

            p['params'] = ["token:"+self.token]
        else:
            p['params'] = []



        if uris:

            p['params'].append(uris)

        if options:

            p['params'].append(options)

        return p



    @staticmethod

    def _defaultErrorHandler(code, message):

        print("ERROR: {}, {}".format(code, message))

        return None

    

    def _post(self, action, params, onSuc, onFail=None):

        if onFail is None:

            onFail = Aria2c._defaultErrorHandler

        payloads = self._genPayload(action, *params)

        resp = requests.post(self.serverUrl, data=json.dumps(payloads))

        result = resp.json()

        if "error" in result:

            return onFail(result["error"]["code"], result["error"]["message"])

        else:

            return onSuc(resp)



    def addUri(self, uri, options=None):

        return self._post(Aria2c.ADD_URI, [[uri,], options], success)



    def getVer(self):

        return self._post(Aria2c.GET_VER, [], success)

    def tellActive(self):

        return self._post('aria2.tellActive', [], success)



    def getFiles(self, gid):

        return self._post('aria2.getFiles', [gid,], success)
