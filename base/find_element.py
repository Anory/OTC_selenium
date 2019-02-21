from util.read_ini import ReadIni


class FindElement(object):
    # 初始化driver
    def __init__(self, driver):
        self.driver = driver

    # 定位元素
    def get_element(self, node, key):
        read_ini = ReadIni()
        data = read_ini.get_value(node, key)
        if data.split('>')[0] not in("className", "linkText", "id", "name"):
            div_class = data.split('>')[0]
            div_class_value = int(data.split('>')[1])
            by = data.split('>')[2]
            element_value = data.split('>')[3]
            div_element = self.driver.find_elements_by_class_name(div_class)[div_class_value]
            try:
                if by == 'id':
                    return div_element.find_element_by_id(element_value)
                elif by == 'name':
                    return div_element.find_element_by_name(element_value)
                elif by == 'className':
                    return div_element.find_element_by_class_name(element_value)
                elif by == 'tagName':
                    return div_element.find_elements_by_tag_name(element_value)
                else:
                    return div_element.find_element_by_xpath(element_value)
            except:
                return None
        else:
            by = data.split('>')[0]
            element_value = data.split('>')[1]
            try:
                if by == 'id':
                    return self.driver.find_element_by_id(element_value)
                elif by == 'name':
                    return self.driver.find_element_by_name(element_value)
                elif by == 'className':
                    return self.driver.find_element_by_class_name(element_value)
                elif by == "linkText":
                    return self.driver.find_element_by_link_text(element_value)
                else:
                    return self.driver.find_element_by_xpath(element_value)
            except:
                return None
