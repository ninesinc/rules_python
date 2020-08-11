import detectron2
import torch
import unittest
import platform


class VersionTest(unittest.TestCase):
    def test_detectron2_version(self):
        self.assertEqual(detectron2.__version__, "0.1.3")

    def test_torch_version(self):
        if platform.system() == "Linux":
            version = "1.5.0+cu101"
        else:
            version = "1.5.0"
        self.assertEqual(torch.__version__, version)


if __name__ == "__main__":
    unittest.main()
