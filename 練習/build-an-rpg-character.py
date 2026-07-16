full_dot = '●'
empty_dot = '○'

def create_character(name, str_stat, int_stat, cha_stat):

    # Name check
    if not isinstance(name, str):
        return 'The character name should be a string'

    if name == '':
        return 'The character should have a name'

    if len(name) > 10:
        return 'The character name is too long'

    if ' ' in name:
        return 'The character name should not contain spaces'

    # Status type check
    if (not isinstance(str_stat, int) or
        not isinstance(int_stat, int) or
        not isinstance(cha_stat, int)):
        return 'All stats should be integers'

    # Range check
    if str_stat < 1 or int_stat < 1 or cha_stat < 1:
        return 'All stats should be no less than 1'

    if str_stat > 4 or int_stat > 4 or cha_stat > 4:
        return 'All stats should be no more than 4'

    # Overall check
    if str_stat + int_stat + cha_stat != 7:
        return 'The character should start with 7 points'

    # Output
    def make_line(label, value):
        return label + ' ' + (full_dot * value + empty_dot * (10 - value))

    return '\n'.join([
        name,
        make_line("STR", str_stat),
        make_line("INT", int_stat),
        make_line("CHA", cha_stat)
    ])