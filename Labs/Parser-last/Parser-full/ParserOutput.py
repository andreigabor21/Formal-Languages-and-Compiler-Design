class ParserOutput:

    def __init__(self, parser):
        # reference of the parser
        self.parser = parser

    def write_parsing_tree(self):
        # prints the parsing tree to the file
        if self.parser.state != "e":
            self.parser.write_in_output_file("\nParsing tree: ")
            self.parser.write_in_output_file("index info parent  left_sibling")
            for index in range(0, len(self.parser.working_stack)):
                message = str(index) + "  " + str(self.parser.tree[index])
                self.parser.write_in_output_file(message)