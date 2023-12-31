from framework.icn_page import ICNPage

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
