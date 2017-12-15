                for varName in self.vars_dict:
                    if node.test.id == varName:
                        print(varName)
                        if self.vars_dict[varName] == 0:
                            #print("HelloWorld")
                            warning = True
                            indirZero = True
                            tempVName = varName
#                            break
                        for key in self.vars_dict.keys():
                            print(key)
                            if self.vars_dict[varName] == key:
                                print(key)