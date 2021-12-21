"""
    This is a utility module.

    To use this module, first import it:

    import util

    Use the read_zip_all() function to read the data
    on ZIP codes:

    zip_codes = util.read_zip_all()
    print(zip_codes[4108])

    Author: Konstantin Kuzmin
    Date: 2/19/2019

"""


def read_zip_all():
    i = 0
    header = []
    zip_codes = []
    zip_data = []
    skip_line = False
    # http://notebook.gaslampmedia.com/wp-content/uploads/2013/08/zip_codes_states.csv
    for line in open('zip_codes_states.csv').read().split("\n"):
        skip_line = False
        m = line.strip().replace('"', '').split(",")
        i += 1
        if i == 1:
            for val in m:
                header.append(val)
        else:
            zip_data = []
            for idx in range(0, len(m)):
                if m[idx] == '':
                    skip_line = True
                    break
                if header[idx] == "latitude" or header[idx] == "longitude":
                    val = float(m[idx])
                else:
                    val = m[idx]
                zip_data.append(val)
            if not skip_line:
                zip_codes.append(zip_data)
    return zip_codes


if __name__ == "__main__":
    zip_codes = read_zip_all()
    # del zip_codes[3]
    # zip_codes[456][1] = None
    # zip_codes[1345][2] = 0.0

    assert len(zip_codes) == 42049, \
        f'The number of ZIP codes read is {len(zip_codes)} instead of 42049'
    print(zip_codes[4108])
    assert zip_codes[4108] == \
        ['12180', 42.673701, -73.608792, 'Troy', 'NY', 'Rensselaer'], \
        'Properties of ZIP 12180 are incorrect'
    print(zip_codes[42048])
    assert zip_codes[42048] == \
        ['99950', 55.542007, -131.432682, 'Ketchikan', 'AK', 'Ketchikan Gateway'], \
        'Properties of ZIP 99950 are incorrect'
    for elem in zip_codes:
        assert elem[1] is not None and elem[1] != 0.0, \
            'Latitude of ZIP {elem[0]} is {elem[1]} which is invalid'
        assert elem[2] is not None and elem[2] != 0.0, \
            'Latitude of ZIP {elem[0]} is {elem[1]} which is invalid'
    print('All tests passed!')
