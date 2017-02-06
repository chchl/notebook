#-*-coding:UTF-8-*-

class Storage(dict):
    def __setattr__(self, key, value):
        self[key] = value
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            return None
    def __defattr__(self, key):
        try:
            del self[key]
        except KeyError:
            return None

    def __call__(self, key):
        try:
            return self[key]
        except KeyError:
            return None

if __name__ == '__main__':
    s = Storage()
    s.name = 'Hello, World'
    print 's.name is %s'%s.name
    print 's("name") is %s' %s("name")
