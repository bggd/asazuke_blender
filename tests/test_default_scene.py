import unittest

from asazuke import asazuke_pb2
import asazuke_blender

class TestDefaultScene(unittest.TestCase):
    def test_default_scene(self):
        a = asazuke_blender.export_asazuke()

        self.assertTrue(isinstance(a, asazuke_pb2.Asazuke))

if __name__ == "__main__":
    import sys
    sys.argv = [__file__]
    unittest.main()
