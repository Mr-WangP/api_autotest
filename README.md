# api_autotest
python + requests + excel + pytest + allure

### 特点

* 使用excel表格记录接口请求信息。
* 测试数据参数化。

### 安装

```shell
$ pip install -r requirements.txt
```

### 配置

在 `config.py` 文件配置

```python
class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录或文件
    cases_path = os.path.join(BASE_PATH, "test_cases", "")

    # 选择测试数据文件
    data_path = os.path.join(BASE_PATH, "data", "case.xlsx")

    # 失败重跑次数
    rerun = "1"

    # 当达到最大失败数，停止执行
    max_fail = "5"
```
在 `case.xlsx` 文件配置接口请求信息

### 运行

```shell
$ python run_tests.py
```
