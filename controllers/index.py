class Index:
    def __call__(self):
        status_code = '200 OK'
        body = b'Hello index page'
        return status_code, body

if __name__ == '__main__':
    index = Index()
    print(index)