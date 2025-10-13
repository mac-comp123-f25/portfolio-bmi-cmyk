def apply_l_system(l_system_dict: dict):
    assert isinstance(l_system_dict, dict)
    assert len(l_system_dict) == 3
    assert "axiom" in l_system_dict
    assert "rules" in l_system_dict
    assert "n" in l_system_dict

    axiom = l_system_dict["axiom"]
    rules = l_system_dict["rules"]
    n = l_system_dict["n"]

    s = axiom
    for _ in range(n):
        s = apply_rules(s, rules)

    return s


def apply_rules(s: str, rules: dict):
    assert type(s) is str
    assert type(rules) is dict

    new_str = ''
    for c in s:
        rule_found = False
        for key in rules:
            if len(key) != 1:
                print("{} -> {} not supported, LHS is not of length "
                      "1".format(key, rules[key]))
                assert False
            if key == c:
                new_str += rules[key]
                rule_found = True
                break

        # no rule
        if not rule_found:
            new_str += c

    return new_str


if __name__ == "__main__":
    l_system_info = {
        'axiom': 'A',
        'rules': {'A': 'B', 'B': 'AB'},
        'n': 0
    }

    for i in range(10):
        l_system_info['n'] = i
        print(apply_l_system(l_system_info))