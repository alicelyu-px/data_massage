import json
import argparse

"""
Expected layout:
    [{'file_attributes': {},
      'filename': 'picture1.png',
      'regions': [{'region_attributes': {},
                   'shape_attributes': {}},
        ... more regions ...
      ],
      'size': xxx},
    ... more pictures ...
    ]
"""

def print_ann(path_to_ann):
    anno = json.load(open(path_to_ann))
    anno = list(anno.values())
    print(anno)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='The path to the exported annotation .json file.')
    parser.add_argument('path',
                        metavar='<path>')
    args = parser.parse_args()
    print_ann(args.path)
