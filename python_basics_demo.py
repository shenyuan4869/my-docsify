"""Python 基础语法示例。

运行：python python_basics_demo.py
"""


def main():
    # 字面量：代码中直接写出的值
    integer_value = 100
    float_value = 3.14
    boolean_value = True
    text_value = "Python"
    empty_value = None

    print("字面量：", integer_value, float_value, boolean_value, text_value, empty_value)

    # 变量是名字与对象之间的绑定；变量名建议使用小写蛇形命名
    user_name = "学习者"
    study_days = 1
    print("变量：", user_name, study_days)

    # 交换两个变量的值
    first_number, second_number = 10, 20
    print("交换前：", first_number, second_number)
    first_number, second_number = second_number, first_number
    print("交换后：", first_number, second_number)

    # 注释不会被 Python 执行，用于解释代码
    print("类型：", type(integer_value).__name__, type(text_value).__name__)


if __name__ == "__main__":
    main()
