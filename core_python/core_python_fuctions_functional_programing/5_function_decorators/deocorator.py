def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


@escape_unicode
def notthern_city():
    return "Tromsø"


print(notthern_city())
