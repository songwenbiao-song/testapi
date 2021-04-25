import random

from tools.api import request_tool
from tools.report.assert_tool import assert_equal


p = '/api/voiceRecordInfo/queryVoiceRecordInfoPage'
def test_post_json(pub_data):
    method = "POST"  # 请求方法，全部大写
    feature = "测试"  # allure报告中一级分类
    story = 'allure报告中二级分类'  # allure报告中二级分类
    title = "allure报告中用例名字"  # allure报告中用例名字
    uri = f"{p}"  # 接口地址    f的使用
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    headers = {'Authorization':'${token}'}
    json_data= {"beginTime": "2021-03-17", "endTime": "2021-03-17", "pageNo": 1, "pageSize": 10, "policeOfficeId": []}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, json_data=json_data, status_code=status_code,
                             expect=expect, feature=feature, story=story, title=title,headers=headers)

    a = r.json()['msg']
    b = '操作成功'
    assert_equal(a,b)
    print('111')
    return a


