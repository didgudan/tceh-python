# -*- coding: utf-8 -*-

# Задача: обрабатывать две версии входных данных для единого запроса.

# ПЕРВАЯ ВЕРСИЯ:
# На вход по адресу "/api/v1/order" приходит json формата:
# Нужно проверить:
# 1) что пришло количество товаров от 1 до 5
# 2) что имя товара находится в списке разрешенных товаров (можно придумать
# список самим)
# 3) что у клиента есть имя
# 4) что пришел непустой адрес
# В конце сохраняем заказ в файл на локальном компьютере

# ВТОРАЯ ВЕРСИЯ:
# На вход по вдресу "/api/v2/order" приходит json вида:
# Нужно проверить:
# 1) что пришло количество товаров от 1 до 10
# 2) что имя товара находится в списке разрешенных товаров (можно придумать
# список самим)
# 3) что у клиента есть непустое имя
# 4) что у клиента есть валидный email
# 5) что пришел непустой адрес
# В конце сохраняем заказ в файл на локальном компьютере. И пишем в лог о
# удачном сохранении.

# В конце сохраняем заказ в файл на локальном компьютере. И пишем в лог о
# удачном сохранении.
# Рекомендуется использовать подход не "в лоб". Потому что всегда может
# появиться версия 2.1, 2.2 и 3.0

import json
import jsonschema

incoming_params = {
    #path: validator path
    "v1_order.json": "v1_schema.json",
    "v2_order.json": "v2_schema.json",
}

log_path = "validation.log"

def return_json_from_file(fname):
    with open(fname) as f:
        json_data = json.load(f)
    return json_data

def add_to_log_message(log_, m):
    with open(log_, "a") as myfile:
        myfile.write(m)

def validate_json():
    for order_path, validator_path in incoming_params.items():
        try:
            order = return_json_from_file(order_path)
            validator = return_json_from_file(validator_path)
            jsonschema.validate(order, validator)
        except jsonschema.ValidationError as e:
            add_to_log_message(log_path, str(e))
        except jsonschema.SchemaError as e:
            print(log_path, str(e))
        else:
            add_to_log_message(
                log_path,
                "Order {} is passed successfully!\n\n".format(order_path)
            )

if __name__ == '__main__':
    validate_json()
