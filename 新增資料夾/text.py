from omeka_s_tools.api import OmekaAPIClient
import json
#omeka = OmekaAPIClient(api_url='http://omekas.ccstw.nccu.edu.tw/api', key_identity='3Hf0y5QQUQqTG0aKPveYsggqbfHXD0u4', key_credential='4kM9IooOeHeC2JKbmsxNRRGzQM9QJtTz')
omeka = OmekaAPIClient(api_url='http://10.0.7.15/api', key_identity='3Hf0y5QQUQqTG0aKPveYsggqbfHXD0u4', key_credential='4kM9IooOeHeC2JKbmsxNRRGzQM9QJtTz')
items = omeka.get_resources('items')
print(items['total_results'])
print(len(items['results']))
#key_identity: 3Hf0y5QQUQqTG0aKPveYsggqbfHXD0u4
#key_credential: 4kM9IooOeHeC2JKbmsxNRRGzQM9QJtTz
test_item = {
    'dcterms:title': [
        {
            'value': 'My first resource!'
        }
    ],
    'dcterms:creator': [
        {
            'value': 'changc'
        }
    ]

}
payload = omeka.prepare_item_payload(test_item)

#print(payload)
#payload_with_media = omeka.add_media_to_payload(payload, media_files=['test.png','test.png'])
#print(payload_with_media['data'][1])
#new_item = omeka.add_item(payload,media_files=['/root/2021-11-30_114408.png','/root/2021-11-30_114408.png'])
#print(new_item)
deleted_resource = omeka.delete_resource('10729', 'items')
print(deleted_resource)
