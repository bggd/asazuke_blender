import unittest

from asazuke import asazuke_pb2
import asazuke_blender

class TestDefaultScene(unittest.TestCase):

    def test_default_scene(self):
        a = asazuke_blender.export_asazuke()

        self.assertTrue(isinstance(a, asazuke_pb2.Asazuke))

        self.assertEqual(len(a.scenes), 1)
        self.assertEqual(a.scenes[0].name, "Scene")

        collection = a.scenes[0].collection
        self.assertEqual(collection.name, "Scene Collection")
        self.assertEqual(len(collection.children), 1)

        child_collection = collection.children[0]
        self.assertEqual(child_collection.name, "Collection")
        self.assertEqual(child_collection.library_file_path, "")

if __name__ == "__main__":
    import sys
    sys.argv = [__file__]
    unittest.main()
