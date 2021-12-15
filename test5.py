
import http.client
import ssl

data='/home/akka_admin/Projects/alsat_docker/inputjson.json'
certificate_file = 'alsatpoc.uksouth.cloudapp.azure.com.cer.pem'
certificate_secret = 'alsatpoc.uksouth.cloudapp.azure.com.key.new.pem'
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=certificate_file, keyfile=certificate_secret)


with open(data) as outfile:
    data = json.load(outfile)
    json_data = json.dumps(data)
    request_url_upload='/uploader'
    headers_req={'Content-Type': 'application/json'}
    connection = http.client.HTTPSConnection('alsatstagnew.esdal2.com', port=443, context=context)
    connection.request('PUT', request_url_upload, json_data, headers_req)
    response2=connection.getresponse()
    print("_______response recalculate________")
    print(response2.read().decode())