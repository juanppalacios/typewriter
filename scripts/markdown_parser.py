#!/usr/bin/env python

import re

# todo: read about parser tools: https://supunsetunga.medium.com/writing-a-parser-getting-started-44ba70bb6cc9

# todo: 'pip install schedule' to run scheduled execution

# todo: images
# todo: listings
# todo: references

def parser():
    print('running our parser...\n')
    
    # open up our markdown file
    markdown_file = []
    latex_file    = []
    
    with open('./src/example.md', 'r') as file:
        markdown_file = file.read()
        
    # section_pattern = r'^#+\s(.+)$'
    section_pattern  = r'^(#+)\s(.+)$'
    sentence_pattern = r'^(?!#)(\S.*)$'
    image_pattern    = r'^(!)(\S.*)$' 
    
    section_matches  = re.findall(section_pattern, markdown_file, flags = re.MULTILINE)
    sentence_matches = re.findall(sentence_pattern, markdown_file, flags = re.MULTILINE)
    image_matches    = re.findall(image_pattern, markdown_file, flags = re.MULTILINE)
    
    # print(section_matches)
    # print(sentence_matches)
    
    print(image_matches)
    
    # note: the biggest issue with this is our title, image, and regular text 
    # note: does not match, i.e., we get mismatched sections, see example.pdf
    
    
    # for each '#' in section matches, include 'sub' 
    with open('./scripts/latex/example.tex', 'w') as file:
        # write out header
        
        file.write("\\documentclass{article}\n\n")
        
        file.write("\\begin{document}\n\n")
        
        for index, heading in enumerate(section_matches):
            file.write(f"\\{'sub' * heading[0].count('#')}section*" + "{" + heading[1] + "}\n")
            file.write(f"{sentence_matches[index]}\n")
            
        # write out 
        file.write("\n\\end{document}")
        
if __name__ == '__main__':
    print("\nWARNING: this script is still under development!\n")
    
    parser()
else:
    pass