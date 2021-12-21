from day10.adv10 import adv10_1, adv10_2, find_closing, find_error, get_missing_chars

syntax_test = [
    ['[', '(', '{', '(', '<', '(', '(', ')', ')', '[', ']', '>', '[', '[', '{', '[', ']', '{', '<', '(', ')', '<', '>', '>'],   # incomp
    ['[', '(', '(', ')', '[', '<', '>', ']', ')', ']', '(', '{', '[', '<', '{', '<', '<', '[', ']', '>', '>', '('],             # incomp
    ['{', '(', '[', '(', '<', '{', '}', '[', '<', '>', '[', ']', '}', '>', '{', '[', ']', '{', '[', '(', '<', '(', ')', '>'],   # error
    ['(', '(', '(', '(', '{', '<', '>', '}', '<', '{', '<', '{', '<', '>', '}', '{', '[', ']', '{', '[', ']', '{', '}'],        # incomp
    ['[', '[', '<', '[', '(', '[', ']', ')', ')', '<', '(', '[', '[', '{', '}', '[', '[', '(', ')', ']', ']', ']'],             # error
    ['[', '{', '[', '{', '(', '{', '}', ']', '{', '}', '}', '(', '[', '{', '[', '{', '{', '{', '}', '}', '(', '[', ']'],        # error
    ['{', '<', '[', '[', ']', ']', '>', '}', '<', '{', '[', '{', '[', '{', '[', ']', '{', '(', ')', '[', '[', '[', ']'],        # incomp
    ['[', '<', '(', '<', '(', '<', '(', '<', '{', '}', ')', ')', '>', '<', '(', '[', ']', '(', '[', ']', '(', ')'],             # error
    ['<', '{', '(', '[', '(', '[', '[', '(', '<', '>', '(', ')', ')', '{', '}', ']', '>', '(', '<', '<', '{', '{'],             # error
    ['<', '{', '(', '[', '{', '{', '}', '}', '[', '<', '[', '[', '[', '<', '>', '{', '}', ']', ']', ']', '>', '[', ']', ']']    # incomp
]

def test_find_closing():
    c0 = find_closing(0, ['(', '{', ']', ')'])
    assert c0 == ')'    # 4th
    c1 = find_closing(0, syntax_test[0])
    assert c1 == None
    c2 = find_closing(0, syntax_test[1])
    assert c2 == ']'    # 10th

def test_find_error():
    e0 = find_error(['(', '{', '}', ')'])
    assert e0 == None    # No error
    e1 = find_error(['(', '{', ']', ')'])
    assert e1 == ']'    # 3rd
    e2 = find_closing(0, syntax_test[1])
    assert e2 == ']'    # 10th

def test_get_missing():
    m0 = get_missing_chars(['[', '(', '{', '}', ')'])
    assert m0 == [']']
    m1 = get_missing_chars(['(', '{', '}', ')'])
    assert m1 == []
    m2 = get_missing_chars(syntax_test[0])
    assert m2 == ['}', '}', ']', ']', ')', '}', ')', ']']

def test_adv10_1():
    val = adv10_1(syntax_test)
    assert val == 26397

def test_adv10_2():
    score = adv10_2(syntax_test)
    assert score == 288957