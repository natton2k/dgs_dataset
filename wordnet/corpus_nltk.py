from nltk.corpus import wordnet

if __name__ == '__main__':
  video_file_path = './data/sign_wordnet_video_gsg.tab'
  gloss_file_path = './data/sign_wordnet_gloss_gsg.tab'
  id_file_path = './data/sign_wordnet_id_gsg.tab'
  poses = ['n', 'a', 's', 'r', 'v']

  video_file = None
  gloss_file = None
  id_file = None

  try:
    video_file = open(video_file_path, mode="r", encoding="utf-8")
    gloss_file = open(gloss_file_path, mode="r", encoding="utf-8")
    id_file = open(id_file_path, mode="r", encoding="utf-8")

    wordnet.custom_lemmas(video_file, "gsg")
    length = len(list(wordnet.words(lang='gsg')))
    print(f'Word with videos: {length}')

    wordnet.custom_lemmas(gloss_file, "gsg")
    length = len(list(wordnet.words(lang='gsg')))
    print(f'Word with gloss: {length}')

    wordnet.custom_lemmas(id_file, "gsg")
    length = len(list(wordnet.words(lang='gsg')))
    print(f'Word with wordnet id: {length}')

  finally:
    if video_file != None:
        video_file.close()
    if gloss_file != None:
      gloss_file.close()
    if id_file != None:
      id_file.close()