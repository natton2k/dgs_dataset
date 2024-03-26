import pandas as pd
import math

def preprocess_csv():
  # read and only keep line that start with dgs
  with open('./data/sign_data.csv', 'r') as input_file:
      with open('./data/dgs_sign_data.csv', 'w') as output_file:
          for line in input_file:
              if line.startswith('dgs'):
                  output_file.write(line)


def main():
  df = pd.read_csv('./data/dgs_sign_data.csv', header=0, quotechar="'")
  print(df.shape)
  non_video_df = df[df['video'].isna()]
  print(non_video_df.shape)
  print(non_video_df.iloc[0]['links'])

if __name__ == '__main__':
  main()
