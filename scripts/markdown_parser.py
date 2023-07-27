#!/usr/bin/env python

import re

# todo: read about parser tools: https://supunsetunga.medium.com/writing-a-parser-getting-started-44ba70bb6cc9


# todo: create a rough but simple parser
def parser():
    print('running our parser...')
    
    # open up our markdown file
    markdown_file = []
    latex_file    = []
    
    with open('example.md', 'r') as file:
        markdown_file = file.read()
        
    # section_pattern = r'^#+\s(.+)$'
    section_pattern  = r'^(#+)\s(.+)$'
    sentence_pattern = r'^(?!#)(\S.*)$'
    
    section_matches  = re.findall(section_pattern, markdown_file, flags = re.MULTILINE)
    sentence_matches = re.findall(sentence_pattern, markdown_file, flags = re.MULTILINE)
    
    # print(section_matches)
    print(sentence_matches)
    
        
    # for each '#' in section matches, include 'sub' 
    with open('simple.tex', 'w') as file:
        # write out header
        
        file.write("\\documentclass{article}\n\n")
        
        file.write("\\begin{document}\n\n")
        
        for index, heading in enumerate(section_matches):
            file.write(f"\\{'sub' * heading[0].count('#')}section*" + "{" + heading[1] + "}\n")
            file.write(f"{sentence_matches[index]}\n")
            
        # write out 
        file.write("\n\\end{document}")
        
# \documentclass{article}
# \begin{document}
# \section*{title}
# \end{document}
if __name__ == '__main__':
    parser()
else:
    pass