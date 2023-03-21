a,b = input().split()

def html_tag(tag):
    def real_decorator(func):
        def wrapper():
            main_txt = func()
            return f"<{tag}>{main_txt}</{tag}>"
        return wrapper
    return real_decorator


@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello World!'

print(hello())  #html_tag(html_tag(hello()))