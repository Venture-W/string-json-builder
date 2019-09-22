
def get_value(obj, key, lowest_key):
    """
    从obj中获取key所对应的值，不存在则根据层级关系自动添加子级对象
    :param obj: 值来源对象
    :param key: 值定位key
    :param lowest_key: key的子级key
    :return:
    """
    log('get value', obj, key, lowest_key)
    dst = obj.copy()
    keys = key.split('.')
    for obj_index, level in enumerate(keys):
        log('level', level)
        # 获取子级key，用于判断子级类型
        if obj_index < keys.__len__() - 1:
            lower_key = keys[obj_index + 1]
        else:
            lower_key = lowest_key
        log('lower_key', lower_key)

        # 根据当前key类型决定list或是dic，设置dst为key对应值
        if is_int(level):
            index = int(level)
            # 假如list长度足够则直接获取目标值，否则根据子级类型添加空对象
            if dst.__len__() > index:
                dst = dst[index]
            else:
                # 填补对象空缺
                append_empty_obj(dst, index, lower_key)
                # 设置返回目标对象
                dst = dst[dst.__len__() - 1]
                log('here', dst)
                log('obj', obj)
        else:
            dst = dst.get(level)
            log('ha', dst)
            log('obj', obj)
            if not dst:
                if is_int(lower_key):
                    dst = []
                else:
                    dst = {}
                # 每次获取均是从根开始，只需要设置根级对象值，其他层级在set方法中设置
                if obj_index == 0:
                    obj[level] = dst
            log('here', dst)
            log('obj', obj)
    log('dst', dst)
    log(obj)
    return dst


def is_int(s):
    """
    判断入参是否为int类型
    :param s: 待评估对象
    :return:
    """
    try:
        int(s)
        return True
    except ValueError:
        pass
    return False


def append_empty_obj(dst, index, lower_key):
    """
    根据lower_key类型判断子级类型，并向dst添加index+1个空子对象
    :param dst:目标对象
    :param index:目标索引
    :param lower_key:子对象key
    :return:
    """
    if is_int(lower_key):
        while dst.__len__() <= index:
            dst.append([])
    else:
        while dst.__len__() <= index:
            dst.append({})


def log(*args):
    """
    记录日志
    :param args:
    :return:
    """
    show_log = False
    if show_log:
        print(args)


def set_value(obj, key, value):
    log('set value', obj, key, value)
    keys = key.split('.')
    if keys.__len__() > 1:
        reverse = key[::-1]
        sub_key = reverse[reverse.index('.') + 1:][::-1]
        current_key = keys[keys.__len__() - 1]
        parent_obj = get_value(obj, reverse[reverse.index('.') + 1:][::-1], current_key)
        if is_int(current_key):
            current_key = int(current_key)
            append_empty_obj(parent_obj, current_key, '')
        log('parent_obj', parent_obj)
        log('current_key', current_key)
        parent_obj[current_key] = value
        set_value(obj, sub_key, parent_obj)
    else:
        if is_int(key):
            key = int(key)
            append_empty_obj(obj, key, '')
        obj[key] = value


if __name__ == '__main__':
    des_json = {'aaa': 'bbb',
                'orderItems': [{'taxRate': 20}]}
    # des_json = {}
    set_value(des_json, 'abc.cba.1', {'ccc': {'bbb': 'hah'}})
    print('result:', des_json)
