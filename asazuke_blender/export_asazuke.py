import bpy
import pathlib
from asazuke import asazuke_pb2

def gen_collection_tree(collection, c: asazuke_pb2.Collection):
    for i in c.children:
        child = collection.children.add()
        child.name = i.name

        if i.library:
            library = i.library
            p = pathlib.Path(library.filepath[2:])
            collection.library_file_path = p.as_posix()

        gen_collection_tree(child, i)



def export_asazuke():
    a = asazuke_pb2.Asazuke()

    for s in bpy.data.scenes:
        scene = a.scenes.add()
        scene.name = s.name

        collection = asazuke_pb2.Collection()

        collection.name = s.collection.name
        if s.collection.library:
            library = s.collection.library
            p = pathlib.Path(library.filepath[2:])
            collection.library_file_path = p.as_posix()

        gen_collection_tree(collection, s.collection)

        scene.collection.CopyFrom(collection)

    return a
