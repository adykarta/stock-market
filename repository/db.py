import riak

myClient = riak.RiakClient(
    pbc_port=8087, host="coordinator", protocol='pbc')
# myClient = riak.RiakClient(pb_port=8087, protocol='pbc')
# myClient = riak.RiakClient(pb_port=8087)
# myClient = riak.RiakClient(pb_port=8087)
