def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
test_function()

#inner_function() - NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?

test_function() # мы вызываем функцию test_function(), которая в свою очередь вызывает inner_function()
# и возвращает нам результат выполнения этой встроенной функции.