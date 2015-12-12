import re
import json
def sum_numbers(text):
    return sum(map(int, re.findall(r'(-?\d+)', text)))

def sum_non_red_numbers(text):
    def sum_partial(node):
        if isinstance(node, int):
            return node
        elif isinstance(node, dict):
            if any(v == 'red' for k, v in node.items()):
                return 0
            else:
                return sum(map(sum_partial, node.values()))
        elif isinstance(node, str):
            return 0
        else:
            assert isinstance(node, list), node
            return sum(map(sum_partial, node))
    return sum_partial(json.loads(text))

assert sum_numbers('[1,2,3]') == sum_numbers('{"a":2,"b":4}') == 6
assert sum_numbers('[[[3]]]') == sum_numbers('{"a":{"b":4},"c":-1}') == 3
assert sum_numbers('{"a":[-1,1]}') == sum_numbers('[-1,{"a":1}]') == 0
assert sum_numbers('[]') == sum_numbers('{}') == 0

print('Sum of all numbers:', sum_numbers(open('12.txt').read()))

assert sum_non_red_numbers('[1,2,3]') == sum_non_red_numbers('{"a":2,"b":4}') == 6
assert sum_non_red_numbers('[[[3]]]') == sum_non_red_numbers('{"a":{"b":4},"c":-1}') == 3
assert sum_non_red_numbers('{"a":[-1,1]}') == sum_non_red_numbers('[-1,{"a":1}]') == 0
assert sum_non_red_numbers('[]') == sum_non_red_numbers('{}') == 0
assert sum_non_red_numbers('[1,{"c":"red","b":2},3]') == 4

print('Sum of all non-red numbers:', sum_non_red_numbers(open('12.txt').read()))
