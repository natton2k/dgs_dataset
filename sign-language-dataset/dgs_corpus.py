import tensorflow_datasets as tfds
import os

tfds.core.utils.gcs_utils._is_gcs_disabled = True
os.environ['NO_GCE_CHECK'] = 'true'

import itertools

from sign_language_datasets.datasets.dgs_corpus import DgsCorpusConfig


def document_level():
  config = DgsCorpusConfig(name="only-annotations", version="1.0.0", include_video=False, include_pose=None)
  dgs_corpus = tfds.load('dgs_corpus', builder_kwargs=dict(config=config))

  from sign_language_datasets.datasets.dgs_corpus.dgs_utils import get_elan_sentences

  for datum in itertools.islice(dgs_corpus["train"], 0, 10):
    elan_path = datum["paths"]["eaf"].numpy().decode('utf-8')
    sentences =  get_elan_sentences(elan_path)

    try:
      sentence = next(sentences)
      print(" ".join([s["gloss"] for s in sentence["glosses"]]))
      print(sentence["german"])
      print()
    except StopIteration:
      pass

def sentence_level():
  config = DgsCorpusConfig(name="only-annotations-sentence-level", version="1.0.0", include_video=False, include_pose=None, data_type="sentence")
  dgs_corpus = tfds.load('dgs_corpus', builder_kwargs=dict(config=config))

  for datum in itertools.islice(dgs_corpus["train"], 0, 5):
    sentence = datum["sentence"]["german"].numpy().decode('utf-8')
    print(sentence)
    print(datum)
    break

def with_video():
  config = DgsCorpusConfig(
    name="only-annotations-sentence-level",
    version="3.0.0",
    include_video=False,
    fps=10,
    include_pose="OpenPose",
    data_type="sentence"
  )
  dgs_corpus = tfds.load('dgs_corpus', builder_kwargs=dict(config=config))

  for datum in itertools.islice(dgs_corpus["train"], 0, 5):
    sentence = datum["sentence"]["german"].numpy().decode('utf-8')
    print(sentence)
    print(datum)

if __name__ == '__main__':
  sentence_level()