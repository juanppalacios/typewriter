#!/usr/bin/env python

# todo: read about parser tools: https://supunsetunga.medium.com/writing-a-parser-getting-started-44ba70bb6cc9


# todo: create a rough but simple parser
def parser():
    print('running our parser...')
    
    # open up our markdown file
    markdown_file = []
    
    with open('example.md', 'r') as file:
        markdown_file = file.readlines()
        
    for line in markdown_file:
        print(line)
        
    # convert our lines to Latex syntax
    latex_file = []
    added_lines = []
    with open('latex/example.tex', 'r') as file:
        latex_file = file.readlines()
        
    for line in markdown_file:
        # todo: use the count() method to then choose how many 'sub' keywords to add
        if '#' in line:
            added_lines.append('\section*')
        
    

if __name__ == '__main__':
    parser()
else:
    pass