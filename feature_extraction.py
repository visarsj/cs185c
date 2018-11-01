import json_lines

posts_features = []  # list of extracted features for each social media post


def extract_features():
    i = 0
    with json_lines.open('training_data/instances.jsonl') as reader:
        for obj in reader:
            features = []
            post_text = obj['postText'][0]

            # feature – number of tokens
            features.append(len(post_text.split()))

            # feature - word length of post text
            features.append(len(post_text))

            # feature - whether the post starts with a number
            if post_text[0].isdigit():
                features.append(1)
            else:
                features.append(0)

            # feature - whether the post ends with a number
            if post_text[-1].isdigit():
                features.append(1)
            else:
                features.append(0)

            # feature – whether the last word ends with a '?' mark
            if post_text[-1] == '?':
                features.append(1)
            else:
                features.append(0)

            # feature – whether the last word ends with a '!' mark
            if post_text[-1] == '!':
                features.append(1)
            else:
                features.append(0)

            # feature – whether the post contains the following key words
            wwwwwwhw = ['who', 'what', 'when', 'where', 'why', 'how', 'which']
            c = 0
            for text in post_text.split():
                if text.lower() in wwwwwwhw:
                    c += 1
                    #print(post_text)
            features.append(c)

            # feature – number of ',' in the post
            c = 0
            for text in post_text.split():
                if ',' in text:
                    c += 1
                    #print(text)
            features.append(c)

            posts_features.append(features)

            # used for testing smaller number of files - delete later
            i += 1
            if i > 100:
                break


def read_file():
    extract_features()

    for features in posts_features:
        print(features)


def main():
    read_file()


if __name__ == '__main__':
    main()
