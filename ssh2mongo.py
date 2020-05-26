from contextlib import contextmanager

from sshtunnel import SSHTunnelForwarder
from pymongo import MongoClient


SSH_HOST = 'ssh_host'
SSH_PORT = 22
SSH_USERNAME = "username"

MONGO_HOST = "mongo_host"
# MONGO_HOST = "spider-mongo-rs-0.mongodb-service.nuts-test-00.svc.cluster.local"
MONGO_PORT= 27017


server = SSHTunnelForwarder(
    ssh_address_or_host=(SSH_HOST, SSH_PORT),
    ssh_username=SSH_USERNAME,
    ssh_pkey="~/.ssh/id_rsa",
    remote_bind_address=(MONGO_HOST, MONGO_PORT),
)


@contextmanager
def mongo_client_proxy():
    server.start()
    port = server.local_bind_port
    client = None
    try:
        client = get_mongo_client(port=port)
        yield client
    finally:
        if client:
            client.close()
        server.close()


def get_mongo_client(host="127.0.0.1", port=27017, username="root", password="root"):

    client = MongoClient(
        host=host,
        port=port,
        username=username,
        password=password,
        minPoolSize=2,
        appname="ssh-tunnel",
        serverSelectionTimeoutMS=30 * 1000,
        socketTimeoutMS=300 * 1000,
        w="majority",
        wTimeoutMS=15000,
        readPreference="primaryPreferred",
        # replicaSet="spiderRepSet",  # 增加该字段将报错
    )
    return client


def test_proxy():
    with mongo_client_proxy() as client:
        resp = client.server_info()
        print(f"resp: {resp}")


if __name__ == '__main__':
    test_proxy()
