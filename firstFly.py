from kazoo.client import KazooClient
import logging

logging.basicConfig()

PATH = "/env/room"
LOCAL_HOST = "127.0.0.1"
zk = KazooClient(hosts='*:2181, *:2182, *:2183'.replace('*', LOCAL_HOST))
zk.start()

#CRUD
#Create
def creat_Path(zk_client_obj, path_var):
    try:
        zk_client_obj.ensure_path(path_var)
    except:
        print("Error on {}".format(creat_Path.__name__))

def creat_Data(zk_client_obj, path_var, data_var):
    try:
        zk_client_obj.create(path_var, data_var.encode(), ephemeral=True)
    except:
        print("Error on {}".format(creat_Data.__name__))
#Read
def read_Data(zk_client_obj, path_var, data_var):
    try:
        if zk_client_obj.exists(path_var):
            data, stat = zk_client_obj.get(data_var)
            print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))
        else:
            print("Data not found :/")
    except:
        print("Error on {}".format(read_Data.__name__))

def read_Children(zk_client_obj, path_var):
    try:
        children = zk_client_obj.get_children(path_var)
        print("There are %s children with names %s" % (len(children), children))
    except:
        print("Error on {}".format(read_Children.__name__))
#Update
def update_Data(zk_client_obj, path_var, data_var):
    try:
        zk_client_obj.set(path_var, data_var.encode())
    except:
        print("Error on {}".format(update_Data.__name__))
#Delete
def delete_Path(zk_client_obj, path_var):
    zk_client_obj.delete(path_var, recursive = True)

def election(zk_client_obj, path_var):
    election = zk_client_obj.Election(path_var, 'test-election')
    election.run(lambda : print("Election Completed...!"))
    print(zk_client_obj.get(path_var))
    print(election.contenders())

creat_Path(zk,PATH)

creat_Data(zk, PATH + "/node2","test2")
creat_Data(zk, PATH + "/node3","test3")
creat_Data(zk, PATH + "/node4","test4")
creat_Data(zk, PATH + "/node5","test5")
creat_Data(zk, PATH + "/node6","test6")
read_Data(zk, PATH, PATH + "/node2")

update_Data(zk, PATH + "/node2", "TeSt2E3")

read_Data(zk, PATH, PATH + "/node2")

read_Children(zk, PATH)

#delete_Path(zk, PATH + "/node2")

#election(zk, PATH + "/node2")

zk.stop()