import requests
from requests_oauthlib import OAuth1

url = 'https://sandboxapi.deere.com/platform/organizations'
auth = OAuth1('johndeere-JcFsHU6CV0klrsgkDHewTLuSAP1QZ2Q8Tx9sFCOs',
              '5b67d63b58a9e80facb93354b18a79eb9be3b668f02e331cace8f5a4190254fa',
               'd8d3c1b7-8f56-4cc3-96a6-0b6da898eea6',
                '19Ryi+uXOFxS3/8Q0h+pHjlGVXaYndLhTOl64Wg4cdA4/5ly0f48DxcN+nBsfFgXP71ruvCHMb4T5fYXeGzQ5uAzGYDKyfONgE0Mp6y1bbA=')
headers = {"Accept":"application/vnd.deere.axiom.v3+json"}
r = requests.get('https://sandboxapi.deere.com/platform/organizations', headers=headers, auth=auth)
data = r.json()


#  create tables
for organization in data['values']:
    #print(organization)
    # insert organization
    #organization = {
    #    id: 1,
    #    name: 'asd',
    #}
    for link in organization['links']:
        if link['rel'] == 'machines':
            rMachine = requests.get(link['uri'], headers=headers, auth=auth)
            dataMachine = rMachine.json()
            for machine in dataMachine['values']:
                # insert machine
                print(machine)
                # machine.organization = organization.id  Relacion entre organization y sus machines


