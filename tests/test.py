import pytest
from framework.icn_page import ICNPage

@pytest.fixture(scope="module")
def icn_page(driver):
    page = ICNPage(driver)
    page.open()
    page.open_icn()
    return page

@pytest.mark.parametrize("version, expected_ram_text", [
    ("4.0", "RAM: 8 GB, and an additional 2 GB for each monitoring point on this computer"),
    ("3.0", "RAM: 4 GB, and an additional 2 GB for each monitoring point on this computer."),
    ("4.0", "объем оперативной памяти: 8 ГБ и по 2 ГБ для каждой точки мониторинга на этом компьютере;"),
    ("3.1", "RAM: 8 GB, and an additional 2 GB for each monitoring point on this computer.")
])

def test_check_sensor_ram(icn_page, version, expected_ram_text):
    icn_page.open_version(version)
    icn_page.open_about()
    icn_page.open_hardware()
    ram_text = icn_page.get_ram_text()
    assert ram_text == expected_ram_text

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo is not None:
        pytest.exit(f"The test '{item.nodeid}' was not completed")

"""
def test_check_sensor_ram_v40(driver):
    icn_page = ICNPage(driver)
    icn_page.open()
    icn_page.open_icn()
    icn_page.open_version_4()
    icn_page.open_about()
    icn_page.open_hardware()
    ram_text = icn_page.get_ram_text_en()
    assert ram_text == "RAM: 8 GB, and an additional 2 GB for each monitoring point on this computer"

def test_check_sensor_ram_v30(driver):
    icn_page = ICNPage(driver)
    icn_page.open()
    icn_page.open_icn()
    icn_page.open_version_3()
    icn_page.open_about()
    icn_page.open_hardware()
    ram_text = icn_page.get_ram_text_en()
    assert ram_text == "RAM: 4 GB, and an additional 2 GB for each monitoring point on this computer."

def test_check_sensor_ram_v40_rus(driver):
    icn_page = ICNPage(driver)
    icn_page.open()
    icn_page.open_icn()
    icn_page.open_version_4()
    icn_page.open_about()
    icn_page.open_hardware()
    ram_text = icn_page.get_ram_text_ru()
    assert ram_text == "объем оперативной памяти: 8 ГБ и по 2 ГБ для каждой точки мониторинга на этом компьютере;"

def test_check_sensor_ram_v31(driver):
    icn_page = ICNPage(driver)
    icn_page.open()
    icn_page.open_icn()
    icn_page.open_version_3.1()
    icn_page.open_about()
    icn_page.open_hardware()
    ram_text = icn_page.get_ram_text_ru()
    assert ram_text == "RAM: 8 GB, and an additional 2 GB for each monitoring point on this computer."
"""
