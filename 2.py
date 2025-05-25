def who_am_i(obj):
    obj_type = type(obj)
    print(f"Тип объекта: {obj_type}")
    print("Атрибуты и методы:")
    for attr in dir(obj):
        print(f"  {attr}")
    is_builtin = (obj_type.__module__ == 'builtins')
    print(f"Встроенный тип: {is_builtin}")
who_am_i(123)
print("---")
who_am_i("hello")
print("---")
who_am_i([1, 2, 3])
