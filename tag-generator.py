'''
tag-generator.py
Copyright 2017 Long Qian
Contact: lqian8@jhu.edu
This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.

Modified by Noto Ootori, 2019.
'''
import getopt
import glob
import os
import sys


POST_DIRS = ['_posts/',]
TAG_DIR = 'tags/'

def main(argv):
    ''' Main function.'''
    try:
        opts, _ = getopt.getopt(argv, '', ['drafts'])
    except getopt.GetoptError:
        sys.exit(1)
    for opt, _ in opts:
        if opt in ['--draft', '--drafts']:
            POST_DIRS.append('_drafts/')

    filenames = []
    for post_dir in POST_DIRS:
        filenames += (glob.glob(post_dir + '*md'))

    total_tags = []
    for filename in filenames:
        f = open(filename, 'r', encoding='utf8')
        crawl = False
        for line in f:
            if crawl:
                current_tags = line.strip().split()
                if current_tags[0] == 'tags:':
                    total_tags.extend(current_tags[1:])
                    crawl = False
                    break
            if line.strip() == '---':
                if not crawl:
                    crawl = True
                else:
                    crawl = False
                    break
        f.close()
    total_tags = set(total_tags)

    old_tags = glob.glob(TAG_DIR + '*.md')
    for tag in old_tags:
        os.remove(tag)
        
    if not os.path.exists(TAG_DIR):
        os.makedirs(TAG_DIR)

    for tag in total_tags:
        tag_filename = TAG_DIR + tag + '.md'
        f = open(tag_filename, 'w')
        write_str = '---\nlayout: tag\ntitle: \"标签: {0}\"\ntag: {0}\n---\n'.format(tag)
        f.write(write_str)
        f.close()
    print("Tags generated, count", len(total_tags))

if __name__ == '__main__':
    main(sys.argv[1:])
