class File(object):
    def __init__(self, filename):
        self.filename = filename
        self.regular_expressions = {}
        self.regex = []
        self.read()

    def read(self):
        with open(self.filename, "r") as file:  
            tokens = None
            final_regex = []
            for line in file:
                if('let' in line):
                    line = line.replace('let ', '')
                    line = line.replace(" ", "")
                    definition, value = line.split('=')
                    value_definition = []
                    if(value[0] == '['):
                        value_definition.append('(')
                        if(value[1] == "'"):
                            separator_counter = value.count('-')
                            if(separator_counter != 0):
                                index_counter = 1
                                first_value = ""
                                second_value = ""
                                first_apostrophe = None
                                second_apostrophe = None
                                while(separator_counter != 0):
                                    if(value[index_counter] == "'" and not first_apostrophe):
                                        first_apostrophe = index_counter
                                    elif(value[index_counter] == "'" and first_apostrophe):
                                        second_apostrophe = index_counter

                                    if(first_apostrophe and second_apostrophe and first_value == ""):
                                        first_value = value[first_apostrophe + 1]
                                        first_apostrophe = None
                                        second_apostrophe = None
                                    elif(first_apostrophe and second_apostrophe and first_value != ""):
                                        second_value = value[first_apostrophe + 1]
                                        first_apostrophe = None
                                        second_apostrophe = None
                                        separator_counter -= 1
                                    
                                    if(first_value != "" and second_value != ""):
                                        first_ascii = ord(first_value)
                                        second_ascii = ord(second_value)
                                        first_value = ""
                                        second_value = ""
                                        if(len(value_definition) > 2):
                                            value_definition.append('|')
                                        for i in range(first_ascii, second_ascii):
                                            value_definition.append(i)
                                            value_definition.append('|')
                                        value_definition.append(second_ascii)

                                    index_counter += 1
                            else:
                                index_counter = 1
                                first_value = ""
                                first_apostrophe = None
                                second_apostrophe = None
                                while(value[index_counter] != ']'):
                                    if(value[index_counter] == "'" and not first_apostrophe):
                                        first_apostrophe = index_counter
                                    elif(value[index_counter] == "'" and first_apostrophe):
                                        second_apostrophe = index_counter
                                    
                                    if(first_apostrophe and second_apostrophe):
                                        first_value = value[(first_apostrophe + 1):second_apostrophe]
                                        first_apostrophe = None
                                        second_apostrophe = None
                                        if(first_value == ''):
                                            first_value = ' '
                                        value_definition.append(first_value)

                                    index_counter += 1

                        elif(value[1] == '"'):
                            index_counter = 2
                            while(value[index_counter] != '"'):
                                if(value[index_counter] == "\\"):
                                    value_definition.append(value[index_counter:(index_counter + 2)])
                                    index_counter += 2
                                else:
                                    ascii_value = ord(value[index_counter])
                                    value_definition.append(ascii_value)
                                    index_counter += 1

                                if(value[index_counter] != '"'):
                                    value_definition.append('|')
                                

                        value_definition.append(')') 
                        self.regular_expressions[definition] = value_definition 
                    else:
                        first_apostrophe = None
                        value_list = []
                        new_string = ""
                        for i in range(len(value) - 1):
                            if(value[i] not in ".|*+?()" and value[i] != "'" and not first_apostrophe):
                                new_string += value[i]
                            elif(value[i] == "'" and not first_apostrophe):
                                first_apostrophe = i
                                if(new_string != ""):
                                    value_list.append(new_string)
                                    new_string = ""
                            elif(value[i] == "'" and first_apostrophe):
                                apostrophes_value = value[(first_apostrophe + 1):i]
                                value_ascii = ord(apostrophes_value)
                                value_list.append(value_ascii)
                                first_apostrophe = None
                            else:
                                if(new_string != ""):
                                    value_list.append(new_string)
                                    new_string = ""
                                
                                if(not first_apostrophe):
                                    value_list.append(value[i])

                        dictionary_keys = list(self.regular_expressions.keys())
                        for i in dictionary_keys:
                            if(i in value_list):
                                element_counter = value_list.count(i)
                                while(element_counter != 0):
                                    index = value_list.index(i)
                                    value_list[index:(index + 1)] = self.regular_expressions[i]
                                    element_counter -= 1
                        bracket_counter = value_list.count("[")
                        while(bracket_counter != 0):
                            initial_bracket = value_list.index("[")
                            final_bracket = value_list.index("]")
                            for i in range((initial_bracket + 1), (final_bracket - 1)):
                                value_list[(i + 1):(i + 1)] = '|'
                            bracket_counter -= 1
                            value_list[initial_bracket] = '('
                            final_bracket = value_list.index("]")
                            value_list[final_bracket] = ')'
                        value_list[0:0] = '('
                        value_list[len(value_list):len(value_list)] = ')'
                        self.regular_expressions[definition] = value_list
                
                elif('rule tokens' in line):
                    tokens = True
                
                elif(tokens):    
                    dictionary_keys = list(self.regular_expressions.keys())
                    if('|' in line):
                        final_regex.append('|')
                    if("'" in line):
                        first_apostrophe = None
                        for i in range(len(line)):
                            if(line[i] == "'" and first_apostrophe == None):
                                first_apostrophe = i
                            elif(line[i] == "'" and first_apostrophe != None):
                                apostrophes_value = line[(first_apostrophe + 1):i]
                                value_ascii = ord(apostrophes_value)
                                final_regex.append(value_ascii)
                                first_apostrophe = None
                    elif('"' in line):
                        first_apostrophe = None
                        for i in range(len(line)):
                            if(line[i] == '"' and first_apostrophe == None):
                                first_apostrophe = i
                            elif(line[i] == '"' and first_apostrophe != None):
                                apostrophes_value = line[(first_apostrophe + 1):i]
                                final_regex.append(apostrophes_value)
                                first_apostrophe = None
                    else:
                        for i in dictionary_keys:
                            if i in line:
                                final_regex[len(final_regex):len(final_regex)] = self.regular_expressions[i]

                        

        self.regex = final_regex
