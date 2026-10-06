from lib.group_chat import *

def test_pytest_setup_complete():
    assert True

def test_groupchat_has_list_of_friends():
    result = group_chat(["Bart", "Lisa"])
    assert result == "Bart" + "&" + "Lisa"