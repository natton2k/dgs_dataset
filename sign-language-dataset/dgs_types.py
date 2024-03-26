import tensorflow_datasets as tfds
import sign_language_datasets.datasets
from sign_language_datasets.datasets.config import SignDatasetConfig

import itertools
import os


tfds.core.utils.gcs_utils._is_gcs_disabled = True
os.environ['NO_GCE_CHECK'] = 'true'


def dgs_types():
  config = SignDatasetConfig(
    name="only-annotations",
    version="3.0.0",
    include_video=True,
    fps=10,
    include_pose=None,
    process_video=False)
  dgs_types = tfds.load('dgs_types', builder_kwargs=dict(config=config))

  for datum in itertools.islice(dgs_types["train"], 0, 11):
    print(datum)
    print('========================')

if __name__ == '__main__':
  dgs_types()