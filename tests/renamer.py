import os


lst = os.listdir("tests")
for ein in lst:
    fcur = ein.replace("about_", "test_")
    os.rename("tests/{}".format(ein), "tests/{}".format(fcur))
