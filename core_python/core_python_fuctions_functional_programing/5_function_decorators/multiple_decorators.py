def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


@decorator1
@decorator2
@escape_unicode
def notthern_city():
    return "Tromsø"


print(notthern_city())
