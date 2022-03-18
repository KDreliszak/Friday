import json


def split_address(address):
    street = None
    housenumber = None

    # handle usage of No, has higer priority than comma
    if ' No ' in address:
        address = address.replace(',', '')
        start_idx = address.find(' No ')
        street = address[:start_idx].strip()
        housenumber = address[start_idx:].strip()

    # handle usage of comma
    elif ',' in address:
        splitted_address = address.split(',')
        # address with multiple commas is incomprehensible
        if len(splitted_address) > 2:
            raise Exception("Unexpected formatting, multiple commas in address")
        temp_list = []
        # the part where biggest percentage are digits is treated as a house number
        for elem in splitted_address:
            temp_list.append({"string": elem, "digit_perct": sum(sign.isdigit() for sign in elem) / len(elem)})
        temp_list = sorted(temp_list, key=lambda e: e['digit_perct'])
        street = temp_list[0]["string"].strip()
        housenumber = temp_list[1]["string"].strip()

    else:
        for index, sign in enumerate(address):
            # string starting with digits
            if sign.isdigit() and index == 0:
                splitted_address = address.split(' ')
                # single or stand alone letter is treated as a part of house number
                if len(splitted_address[1]) < 2:
                    housenumber = ' '.join([splitted_address[0], splitted_address[1]]).strip()
                    street = (' '.join(elem for elem in splitted_address[2:])).strip()
                else:
                    housenumber = splitted_address[0].strip()
                    street = (' '.join(elem for elem in splitted_address[1:])).strip()
                break
            # string with digits not at the start
            elif sign.isdigit() and index != 0:
                street = address[:index].strip()
                housenumber = address[index:].strip()
                break

    if street and housenumber:
        json_object = json.dumps({"street": street, "housenumber": housenumber})
        return json_object
    else:
        raise Exception("Provided address was unreadable")


address = input("Input address: ")
