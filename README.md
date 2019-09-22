# string-json-builder

根据字符串生成对应的json/dict(字典)对象
例：
  des_json = {'aaa': 'bbb',
              'orderItems': [{'taxRate': 20}]}
  set_value(des_json, 'abc.cba.1', {'ccc': {'bbb': 'hah'}})
  print('result:', des_json)
  // result: {'aaa': 'bbb', 'orderItems': [{'taxRate': 20}], 'abc': {'cba': [{}, {'ccc': {'bbb': 'hah'}}]}}
