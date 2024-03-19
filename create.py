#!/usr/bin/python3

def create(self, args): 
    """ Create an object of any class""" 
    # split args string into list of strings 
    arg_list = args.split() 
    class_name = '' 
    if len(arg_list) >= 1: 
        if arg_list[0] not in HBNBCommand.classes: 
            print("** class doesn't exist **") 
            return 
        else: 
            class_name = arg_list[0]
            # Omit class name from list of args 
            params = arg_list[1:] 
            # checks for paramter requirment(<key>=<value>) 
            # and puts them in a sublist 
            params[:] = [x.split('=') for x in params if '=' in x] 
            # check if length of sublists is more than 2 
            # or contains empty strings created split() from 
            # trying to split '=' without values before or after '=' 
            params[:] = [x for x in params if len(x) == 2 and '' not in x] 
            # find and convert values in sublist that are floats 
            #  or ints into proper datatype 
            for val in params:
                if val[1].isdigit(): 
                     val[1] = int(val[1]) 
                else: 
                    try:
                        float(val[1]) 
                        val[1] = float(val[1]) 
                    except ValueError: 
                        pass 
            # omit sublists(contains key and value) that 
            # dont match the requirements: 
            # <key> must not be in double quote 
            # <value> that are strings must be in doublequotes 
            newlist = [] 
            for each in params: 
                # checks if <key> is not in double quotes, 
                # then appends to newlist 
                if each[0][0] != '\"' and each[0][-1] != '\"': 
                    if type(each[1]) is float or type(each[1]) is int:
                        newlist.append(each) 
                    # checks if <value> matches requirement for string type, 
                    # then appends to newlist 
                elif type(each[1]) is str: 
                    if each[1][0] == '\"' and each[1][-1] == '\"': 
                        each[1] = each[1][1:-1] 
                        newlist.append(each) 
            new_instance = HBNBCommand.classes[class_name]() 
            for attrs in newlist: 
                if type(attrs[1]) is str:
                    # replace underscores with space 
                    attrs[1] = attrs[1].replace('_', ' ') 
                        # escape doublequotes 
                    attrs[1] = attrs[1].replace('"', '\"')
                    setattr(new_instance, attrs[0], attrs[1]) 
            new_instance.save() 
            print(new_instance.id) 
            # storage.save()
    else:
        # print("in here") 
        if not args: 
            print("** class name missing **") 
            return
        elif args not in HBNBCommand.classes: 
            print("** class doesn't exist **") 
            return


if __name__ == '__main__':
    create(create, args)
