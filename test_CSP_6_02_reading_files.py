import CSP_6_02_reading_files as HW

def test_longest_line():
    assert HW.longestLine("./January - Feb/6-02-reading-files-HM-mmmm-main/ExampleText.txt") == ("how do you do this stuff")
    assert HW.longestLine("/Users/hayden/PycharmProjects/PythonProject/AP_Principles_2026/January - Feb/6-02-reading-files-HM-mmmm-main/ExampleText.txt") == ("how do you do this stuff")

def test_to_binary():
    assert HW.toBinary("./January - Feb/6-02-reading-files-HM-mmmm-main/binary.txt") == (["11111111","00000000","11111111","0000","10101010","01010101","10101010"])
    assert HW.toBinary("/Users/hayden/PycharmProjects/PythonProject/AP_Principles_2026/January - Feb/6-02-reading-files-HM-mmmm-main/binary.txt") == (["11111111","00000000","11111111","0000","10101010","01010101","10101010"])