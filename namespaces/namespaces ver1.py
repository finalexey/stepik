
namespaces = {'global': {'parent': None,
                         'children': [],
                         'vars': []}
              }


def get(namespace, var):
    if namespace not in namespaces or namespace is None:
        print(None)
        return None
    elif var in namespaces[namespace]['vars']:
        print(namespace)
    elif var not in namespaces[namespace]['vars']:
        return get(namespaces[namespace]['parent'], var)


def add(namespace, var):
    if namespace is None or namespace not in namespaces:
        return None
    elif namespace in namespaces and var not in namespaces[namespace]['vars']:
        namespaces[namespace]['vars'].append(var)


def create(namespace, parent):
    namespaces[parent]['children'].append(namespace)
    namespaces[namespace] = {'parent': parent,
                             'children': [],
                             'vars': []}


s = int(input())
while s > 0:
    cmd, namespace, arg = input().split()
    if cmd == 'create':
        create(namespace, arg)
    elif cmd == 'add':
        add(namespace, arg)
    elif cmd == 'get':
        get(namespace, arg)
    s -= 1
