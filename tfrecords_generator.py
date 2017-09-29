"""
this script is used to generate tfrecords. it contains a function,
the input data is a map.
example:  key: path/to/your/images  value: 0
"""


class TFRecordsGenerator(object):
    def __init__(self, url_map, out_path):
        """
          Args
              url_map:
              out_path:output path for tfrecords
        """
        self.url_map = url_map
        self.out_path = out_path

    """
    generate tfrecord 
    
    """

    def generate(self):
        """
        start to generate tfrecords from url_map
        :return:
        """
